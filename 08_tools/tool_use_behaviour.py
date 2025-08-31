from agents import Agent, Runner, trace, enable_verbose_stdout_logging
import asyncio
from tools.wish_birthday_tool import wish_birthday
from tools.greeting import greeting_kro
from my_config import config


async def advance(input_text: str):
    enable_verbose_stdout_logging()
    agent = Agent(
        name="Birthday Wishing Agent",
        instructions="You are an agent that wish birthday to user.",
        tools=[wish_birthday, greeting_kro],
        tool_use_behavior="run_llm_again",
    )
    with trace("tool_use_behaviour"):
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
