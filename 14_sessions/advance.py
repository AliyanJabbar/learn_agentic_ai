# with streaming
import asyncio
from agents import Agent, Runner, SQLiteSession
from openai.types.responses import ResponseTextDeltaEvent
from my_config import config


async def main():
    # Create an agent
    agent = Agent(name="Assistant", instructions="Reply very concisely.")

    # Create a session instance that will persist across runs
    session = SQLiteSession("conversation_123")

    while True:
        print("session: ", await session.get_items())
        user_input = input("User:")
        result = Runner.run_streamed(agent, input=user_input,run_config=config,session=session)
        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(
                event.data, ResponseTextDeltaEvent
            ):
                print(event.data.delta, end="", flush=True)



if __name__ == "__main__":
    asyncio.run(main())

