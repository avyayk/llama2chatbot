# Create a singleton Pinecone client instance
# -- design choice, while violating dependency inversion principle, prevents multiple client instances (which may cost, idk...)

# ~ Imports ~
from pinecone import Pinecone

# ~ Environment management
from dotenv import find_dotenv, load_dotenv
import os

# ~ Singleton functionality
from utilities.decorators import SingletonClass

@SingletonClass
class PineconeClient( Pinecone ):
    
    # Initialize with API key & environment from .env
    def __init__(self):

        # Get environment variables and initialize class object
        apiKey, environment = os.getenv( 'PINECONE_API_KEY'), os.getenv( 'PINECONE_ENVIRONMENT' )
        super().__init__(
            api_key = apiKey,
            environment = environment
        )