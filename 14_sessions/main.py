import asyncio
from agents import Agent, Runner, SQLiteSession
from my_config import config


async def main():
    # Create an agent
    agent = Agent(name="Assistant", instructions="Reply very concisely.")

    # Create a session instance that will persist across runs
    session = SQLiteSession("conversation_123")

    while True:
        print("session: ", await session.get_items())
        user_input = input("User:")
        result = await Runner.run(agent, user_input, session=session, run_config=config)
        print(f"Assistant: {result.final_output}")
        print()


if __name__ == "__main__":
    asyncio.run(main())
