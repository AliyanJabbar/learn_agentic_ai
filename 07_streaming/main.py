from agents import Agent, Runner
from openai.types.responses import ResponseTextDeltaEvent
import asyncio
from my_config import config



async def main():
    agent = Agent(name="Assistant", instructions="You are a helpful assistant.")

    # result = Runner.run_streamed(agent, input="Please tell me 5 jokes.",)
    result = Runner.run_streamed(
        starting_agent=agent,
        input="Please tell me 1 joke.",
        run_config=config,
    )
    print("result: ", result)
    print("result.final_output: ", result.final_output)
    async for event in result.stream_events():
        # print("event:", event)
        if event.type == "raw_response_event" and isinstance(
            event.data, ResponseTextDeltaEvent
        ):
        # if event.type == "raw_response_event" and type(event.data) == ResponseTextDeltaEvent:
            print(event.data.delta, end="", flush=True)
            # print("event:", event)
            # print("event.data:", event.data)
            # print("event.data.delta:", event.data.delta)

asyncio.run(main())

