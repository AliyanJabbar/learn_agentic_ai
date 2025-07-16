from dotenv import load_dotenv
import os
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_default_openai_api,
    set_default_openai_client,
    set_tracing_disabled,
)

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")

if not gemini_key:
    raise ValueError("Api key is not set")


external_client = AsyncOpenAI(
    api_key=gemini_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_default_openai_client(client=external_client, use_for_tracing=False)
set_default_openai_api("chat_completions")
set_tracing_disabled(disabled=True)

# urdu agent
urdu_agent = Agent(
    name="Urdu agent", instructions="You only speak Urdu.", model="gemini-2.0-flash"
)

# chinese agent
chinese_agent = Agent(
    name="Chinese agent",
    instructions="You only speak Chinese.",
    model="gemini-2.0-flash",
)

# english agent
english_agent = Agent(
    name="English agent",
    instructions="You only speak English",
    model="gemini-2.0-flash",
)

# main agent
triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    model="gemini-2.0-flash",
    handoffs=[urdu_agent, english_agent, chinese_agent],
)
# "السلام عليكم" for testing with urdu
# "hello" for testing with english
# "Nǐ hǎo" for testing with chinese

input = input("say something in your language: ")
result = Runner.run_sync(triage_agent, input=input)
print("final output: ", result.final_output)
print("last agent: ", result.last_agent)
