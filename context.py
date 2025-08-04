import asyncio
from dataclasses import dataclass
import os
from dotenv import find_dotenv, load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, RunContextWrapper, Runner, function_tool

load_dotenv(find_dotenv())

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-2.0-flash"
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"


client = AsyncOpenAI(api_key=GEMINI_API_KEY, base_url=BASE_URL)
model = OpenAIChatCompletionsModel(model=MODEL, openai_client=client)

# -------------------- Context class --------------------
@dataclass
class User:
    name:str
    age:int
    id: int

# -------------------- Tool to get data from context -------------------- 
@function_tool
def get_user_age(wrapper:RunContextWrapper[User]) -> str:
    """Return user's age"""
    return f'{wrapper.context.name} is {wrapper.context.age} years old.'

# -------------------- Main agent --------------------  
agent = Agent[User](
    name='Personal Assistant',
    instructions='You are a helpful assistant. Use the tools provided to answer questions.',
    tools=[get_user_age],
    model=model
)

async def main():
    try:
        user = User('Saad',18, 105)  # object
        
        res = await Runner.run(
            starting_agent=agent,
            input='what is the name of the user?',
            context=user
        )
        print(res.final_output)
    except Exception as e:
        print('you cannot use tools with structue output on same agent using gemini model')
        print(f'An Error occured: {e}')


if __name__ == "__main__":
    asyncio.run(main())