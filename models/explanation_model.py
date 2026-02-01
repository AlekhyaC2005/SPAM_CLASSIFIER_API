# IMPORT LIBRARIES
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# LOADING ENV VARIABLES
load_dotenv()
GROQ_API_KEY=os.getenv("GROQ_API_KEY")

# MODEL
chat_model=ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.1-8b-instant"
)
