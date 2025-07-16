from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)
import os
from dotenv import load_dotenv
import asyncio
from tools.wish_birthday_tool import wish_birthday


async def main(input_text: str):
    load_dotenv()
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise ValueError("GEMINI_API_KEY missing")

    external_client = AsyncOpenAI(
        api_key=key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    model = OpenAIChatCompletionsModel(
        model="gemini-1.5-flash",
        openai_client=external_client,
    )

    agent = Agent(
        name="Birthday Wishing Agent",
        instructions="You are an agent that wish birthday to others, you mush take age and name to wish someone a happy birthday.",
        model=model,
        tools=[wish_birthday],
    )

    set_tracing_disabled(True)

    result = await Runner.run(starting_agent=agent, input=input_text)
    print("Final output:", result.final_output)

async def run_interactive():
    """Run the interactive loop within a single event loop"""
    while True: 
        user_input = input("Enter your input: ")
        if user_input.lower() == "exit":
            break
        await main(user_input)

if __name__ == "__main__":
    asyncio.run(run_interactive())
