from agents import Agent, Runner, enable_verbose_stdout_logging, ModelSettings
import asyncio
from tools.wish_birthday_tool import wish_birthday
from my_config import config


async def advance(input_text: str):
    enable_verbose_stdout_logging()
    agent = Agent(
        name="Birthday Wishing Agent",
        # instructions="You are an agent that wish birthday to others, you mush take age and name to wish someone a happy birthday.",
        instructions="You are an agent that wish birthday to user.",
        tools=[wish_birthday],
        # model_settings=ModelSettings(tool_choice="required"),
    )

    result = await Runner.run(agent, input_text, run_config=config)
    print("Final output:", result.final_output)


async def run_interactive():
    """Run the interactive loop within a single event loop"""
    while True:
        user_input = input("Enter your input: ")
        if user_input.lower() == "exit":
            break
        await advance(user_input)


if __name__ == "__main__":
    asyncio.run(run_interactive())
