import asyncio
import random
from agents import Agent, Runner, function_tool
from openai.types.responses import ResponseTextDeltaEvent
from my_config import config


@function_tool
def how_many_jokes() -> int:
    print("tool running...")
    return random.randint(1, 5)


@function_tool
def fetch_weather() -> str:
    print("tool running...")
    return "hi"


async def advance():
    handoff_agent = Agent(
        name="Handoff",
        instructions="First call the `how_many_jokes` tool, then tell that many jokes. Make random jokes and then tell it to user.",
        tools=[how_many_jokes],
    )
    agent = Agent(
        name="Joker",
        instructions="First call the `how_many_jokes` tool, then tell that many jokes. Make random jokes and then tell it to user.",  # to test if how_many_jokes tool was called
        # instructions="First call the `fetch_weather` tool and then tell it to user.",  # to test if fetch weather tool was called.
        # instructions="You are supportive agent.",
        handoffs=[handoff_agent],
        tools=[how_many_jokes, fetch_weather],
    )
    while True:
        user_input = input("Message: ")
        result = Runner.run_streamed(agent, input=user_input, run_config=config)
        print("=== Run starting ===")

        async for event in result.stream_events():
            # When the agent updates, print that
            if event.type == "raw_response_event" and isinstance(
                event.data, ResponseTextDeltaEvent
            ):
                print(event.data.delta, end="", flush=True)
            # elif event.type == "agent_updated_stream_event":
            # print(f"Agent updated: {event.new_agent.name}")
            # print(f"agent updated stream event: {event}")

            # When items are generated, print them
            elif event.type == "run_item_stream_event":
                # print("event run item: ", event)
                if event.item.type == "tool_call_item":
                    # print("event :  ", event)
                    print("event.item :  ", event.item)
                    print("----", event.item.raw_item.name, "tool was called")
                    print("-- Tool was called")
                elif event.item.type == "tool_call_output_item":
                    print(f"-- Tool output: {event.item.output}")
                pass
            # else:
            #     # print("unmatched event")  # Ignore other event types
            #     pass
        print("=== Run complete ===")


if __name__ == "__main__":
    print("Running...")
    asyncio.run(advance())
