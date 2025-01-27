from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.embedder.openai import OpenAIEmbedder
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.lancedb import LanceDb, SearchType
from phi.model.ollama import Ollama

def create_agent_with_pdf(pdf_url):
        """
        Dynamically creates an Agent with a knowledge base from a given PDF URL.

        :param pdf_url: URL to the PDF file
        :return: Configured Agent object
        """
        knowledge_base = PDFUrlKnowledgeBase(
        urls=[pdf_url],
        vector_db=LanceDb(
                table_name="table_temp",
                uri="tmp/lancedb",
                search_type=SearchType.vector,
                embedder=OpenAIEmbedder(model="text-embedding-3-small"),
        ),
        )

        knowledge_base.load()

        agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        knowledge=knowledge_base,
        show_tool_calls=True,
        markdown=True,
        )


        return agent