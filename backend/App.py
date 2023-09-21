# ~ API Application to serve chatbot to a UI interface ~

# ~ Imports ~

# > API imports
from fastapi import FastAPI
from pydantic import BaseModel

# # > LangChain imports
# from langchain.llms import Replicate
# from langchain.vectorstores import Pinecone
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.document_loaders import PyPDFLoader
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.chains import ConversationalRetrievalChain

# # > PineCone client
# import pinecone

# > Environment management (.env support)
from dotenv import find_dotenv, load_dotenv


# ~ Load .env on startup (it'll "find" it in the main directory)
load_dotenv( find_dotenv() )

# ~ Create FastAPI application
API = FastAPI()

# ~ 

# ~ Main process (for running Uvicorn server) ~
if __name__ == '__main__':
    # TODO
    pass