# 1. With synchronous method
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
import os
# from agents.run import RunConfig

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env')) #getting env from parent

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", openai_client=external_client
)

config = RunConfig(model=model, model_provider=external_client, tracing_disabled=True)

agent: Agent = Agent(name="Assistant", instructions="You are a helpful assistant")

result = Runner.run_sync(agent, "Hello, how are you.", run_config=config)

print(result.final_output)


# 2. With asyncronous method
import asyncio
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
import os
# from agents.run import RunConfig

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env')) #getting env from parent

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


async def main():

    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash", openai_client=external_client
    )

    config = RunConfig(
        model=model, model_provider=external_client, tracing_disabled=True
    )

    agent: Agent = Agent(name="Assistant", instructions="You are a helpful assistant")

    result = await Runner.run(agent, "Hello, how are you.", run_config=config)

    print(result.final_output)


asyncio.run(main())
