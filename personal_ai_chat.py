from openai import OpenAI
import streamlit as st
from aws_upload import upload_to_s3
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.embedder.openai import OpenAIEmbedder
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.lancedb import LanceDb, SearchType
from personal_ai_agent import create_agent_with_pdf

client = OpenAI()

# Function to initialize the Streamlit sidebar and handle PDF upload
def handle_sidebar():
    """
    Handles the sidebar, file upload, and returns the uploaded PDF URL.
    """
    with st.sidebar:
        uploaded_file = st.file_uploader("Choose a file", type=["pdf"])
        pdf_url = None

        if uploaded_file is not None:
            pdf_url = upload_to_s3(uploaded_file, bucket="perconal-ai-agent-pdfs", object_name=uploaded_file.name)
            if pdf_url:
                st.success("File uploaded successfully!")
                print(pdf_url)

    return pdf_url


# Function to initialize the AI agent
def initialize_agent(pdf_url):
    """
    Initializes the agent with the uploaded PDF URL.
    """
    if "agent" not in st.session_state and pdf_url:
        st.session_state.agent = create_agent_with_pdf(pdf_url)


# Function to initialize the chat messages
def initialize_messages():
    """
    Initializes the message history in session state.
    """
    if "messages" not in st.session_state:
        st.session_state.messages = []


# Function to display chat history
def display_chat_history():
    """
    Displays the chat message history from session state.
    """
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


# Function to handle user input and generate a response
def handle_user_input():
    """
    Handles user input and generates a response from the AI agent.
    """
    if prompt := st.chat_input("Ask something based on the uploaded PDF"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate AI response
        if "agent" in st.session_state:
            with st.chat_message("assistant"):
                response = st.session_state.agent.run("Based on the given PDF only, " + prompt, markdown=True)
                st.markdown(response.content)

            # Store the assistant's response in the session state
            st.session_state.messages.append({"role": "assistant", "content": response.content})
        else:
            st.error("No PDF uploaded. Please upload a PDF.")


# Main function to run the Streamlit app
def main():
    """
    Main function to run the Personal AI Agent app.
    """
    st.title("Personal AI Agent")
    pdf_url = handle_sidebar()
    initialize_agent(pdf_url)
    initialize_messages()
    display_chat_history()
    handle_user_input()


if __name__ == "__main__":
    main()
