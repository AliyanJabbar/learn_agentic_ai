import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from openai.types.responses import ResponseTextDeltaEvent
import asyncio


from dotenv import load_dotenv


async def main():

    load_dotenv()
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    # Check if the API key is present; if not, raise an error
    if not gemini_api_key:
        raise ValueError(
            "GEMINI_API_KEY is not set. Please ensure it is defined in your .env file."
        )

    # Reference: https://ai.google.dev/gemini-api/docs/openai
    external_client = AsyncOpenAI(
        api_key=gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash", openai_client=external_client
    )

    config = RunConfig(
        model=model, model_provider=external_client, tracing_disabled=True
    )

    agent = Agent(name="Joker", instructions="You are a helpful assistant.")

    # result = Runner.run_streamed(agent, input="Please tell me 5 jokes.",)
    result = Runner.run_streamed(
        starting_agent=agent,
        input="Please tell me 5 jokes.",
        run_config=config,
    )
    print("result: ", result)
    print("result.final_output: ", result.final_output)
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(
            event.data, ResponseTextDeltaEvent
        ):
            # print(event.data.delta, end="", flush=True)
            # print("event:", event)
            # print("event.data:", event.data)
            print("event.data.delta:", event.data.delta)


asyncio.run(main())
