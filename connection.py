from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
import os
import rich
# Load environment variables from .env file
load_dotenv()
# Get the OpenAI API key from environment variables
api_key = os.getenv('GEMINI_API_KEY')
MODEL = 'gemini-2.0-flash'
if not api_key:
    raise ValueError('Gemini API key is not set in the environment variables.' )

# Initialize external client for Gemini
external_client = AsyncOpenAI(
    api_key=api_key,
    base_url='https://generativelanguage.googleapis.com/v1beta/openai'
)

# DEfine the model Configuration
model = OpenAIChatCompletionsModel(
    model=MODEL,
    openai_client=external_client
)

# Define the run configuration
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
    
)

