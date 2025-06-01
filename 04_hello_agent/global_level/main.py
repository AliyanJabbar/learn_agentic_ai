from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_default_openai_client,
    set_tracing_disabled,
    set_default_openai_api,
)
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env')) #getting env from parent

gemini_api_key = os.getenv("GEMINI_API_KEY")


set_tracing_disabled(True)
set_default_openai_api("chat_completions")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_default_openai_client(external_client)

agent: Agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model="gemini-2.0-flash",
)

result = Runner.run_sync(agent, "How are you ?")

print(result.final_output)
