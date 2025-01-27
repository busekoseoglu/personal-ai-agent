# Personal AI Agent

![EkranKayd2025-01-2415 17 32-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/d17d52f7-570f-479a-8649-f9fe90422b05)

## Technologies Used in the Streamlit Application

This Streamlit application leverages various technologies to create an interactive and intelligent interface. Below are the technologies used and their explanations:

---

## 1. Streamlit

**Purpose**:  
Used to create a web-based interface. Streamlit enables quick transformation of data science and machine learning projects into interactive applications.

**What It Does in the Code**:
- Allows users to upload a PDF file (`st.file_uploader`).
- Captures user inputs (`st.chat_input`) and displays them in a chat-style interface (`st.chat_message`).

---

## 2. OpenAI API

**Purpose**:  
Integrates natural language processing (NLP) capabilities using OpenAI's GPT-4-based language model.

**What It Does in the Code**:
- Communicates with the OpenAI API to generate responses for user inputs.

---

## 3. Phi Library

Phi is a library designed to combine data processing, knowledge bases, and AI models. Several modules from Phi are utilized:

### a. **Agent**

**Purpose**:  
Creates an "agent" by combining the ChatGPT model with a knowledge base.

**What It Does in the Code**:
- Answers user queries using a language model connected to a knowledge base.

### b. **PDFUrlKnowledgeBase**

**Purpose**:  
Processes and indexes PDFs, converting their content into vectors to serve as a queryable knowledge base.

**What It Does in the Code**:
- Processes uploaded PDF files to create a searchable knowledge base.

### c. **LanceDb**

**Purpose**:  
Provides a lightweight and fast vector database to store vectors extracted from PDFs.

**What It Does in the Code**:
- Stores PDF content in vector format and enables fast searches for queries.

### d. **OpenAIEmbedder**

**Purpose**:  
Uses OpenAI's embedding model (`text-embedding-3-small`) to convert PDF content into text vectors.

**What It Does in the Code**:
- Generates text-based embeddings for the knowledge base.

---

## 4. AWS S3

**Purpose**:  
Used to store uploaded PDF files in the cloud.

**What It Does in the Code**:
- The `upload_to_s3` function uploads the user's PDF file to an Amazon S3 bucket.

---

## 5. OpenAIChat (Phi Model)

**Purpose**:  
Utilizes `gpt-4o-mini` as the agent's language model, an optimized version of GPT-4.

**What It Does in the Code**:
- Analyzes user queries and provides appropriate responses using the knowledge base.

---

## 6. Vector-Based Search

**Purpose**:  
Uses vector-based querying to search the knowledge base for user questions.

**What It Does in the Code**:
- Converts the user's question into embeddings and searches for similar content in the knowledge base.

---

## Workflow Between Technologies

1. The user uploads a PDF file (via Streamlit).  
2. The file is uploaded to AWS S3.  
3. The PDF content is processed and converted into vectors using Phi library modules (with `OpenAIEmbedder` and `LanceDb`).  
4. The agent searches the vector-based knowledge base for relevant information.  
5. The response is displayed to the user via the Streamlit interface.

---

This integration of modern NLP and knowledge base technologies creates a powerful foundation for building customizable, knowledge-driven chatbots. The application demonstrates how cutting-edge AI and database technologies can come together to deliver an interactive user experience.
