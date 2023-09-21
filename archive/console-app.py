
# Document chatbot using Llama2

# imports
import os, sys

# TODO: needs setup
import pinecone # Need an API key!

# langchain imports
from langchain.llms import Replicate
from langchain.vectorstores import Pinecone
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain
# from langchain.document_loaders import WebBaseLoader

# Streamlit Replicate API token
os.environ[ 'REPLICATE_API_TOKEN' ] = "r8_bqQJYeM822tRc5k3VVpJbrmaSFpgS0W251p7I"

# Initialize Pinecone client
pinecone.init( 
    api_key = '5e88ce0f-0661-406b-bc9f-4000575d858d',
    environment = 'gcp-starter'
)

# ~ Getting the data to build our chatbot ~

# Load and preprocess PDF document
pdfLoader = PyPDFLoader( 'BERT.pdf' )
documents = pdfLoader.load()

# Split the document into smaller chunks for processing
textSplitter = CharacterTextSplitter( chunk_size = 1000, chunk_overlap = 0 )
texts = textSplitter.split_documents( documents )

# HuggingFace word embeddings (transforming the text into tensors)
embeddings = HuggingFaceEmbeddings()

# Creating the Pinecone vector database
indexName = "llama2-pdf-chatbot" # TODO
index = pinecone.Index( indexName )
vectorDB = Pinecone.from_documents( texts, embeddings, index_name = indexName )

# Initialize Replicate Llama2 Model
LLM = Replicate(
    model = "a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5", # NOTE; Taking on good faith that this key is correct
    input = { 
        "temperature": 0.75, 
        "max_length": 3000 
    }
)

# We combine Llama2 model and Pinecone vector DB to create a dynamic and interactive chatbot
qaChain = ConversationalRetrievalChain.from_llm( 
    LLM,
    vectorDB.as_retriever( search_kwargs = {'k': 2} ),
    return_source_documents = True
)

# Driver
chatHistory = []

exitPhrases = { "exit", "quit", "q" }

# Live chatbot
while True:
    textQuery = input( 'Prompt: ' )

    # To exit the application
    if textQuery.lower() in exitPhrases:
        print( "Terminating...")
        sys.exit()

    # Chatbot response
    response = qaChain( { 'question': textQuery, 'chat_history': chatHistory } )
    print( f'Answer: { response["answer"] }\n' )

    # Update chat history
    chatHistory.append( ( textQuery, response['answer'] ) )

# NOTE: Now that we have this out-of-the-box functionality, why don't we productionalize it?