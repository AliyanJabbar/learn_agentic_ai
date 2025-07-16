from dotenv import load_dotenv
import os
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_default_openai_api,
    set_default_openai_client,
    set_tracing_disabled,
    RunContextWrapper,
    handoff,
    enable_verbose_stdout_logging,
)
from pydantic import BaseModel

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
enable_verbose_stdout_logging()  # shows that at firt the agent has 3 handoffs. Each handoff agent is treated as tools with name = transfer_to_"agent_name". then the agent decides to transfer to which agent and then the response is generated.
# urdu agent
urdu_agent = Agent(
    name="Urdu agent", instructions="You only speak Urdu.", model="gemini-2.0-flash"
)


# schema for chinese agent
class validate_chinese(BaseModel):
    chinese_message: str


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


# single onhandoff function for configuration
def Handoff_ka_kaam(agent: Agent, wrapper: RunContextWrapper[None]):
    print("--------------------------------")
    print(f"Handing off to {agent.name}...")
    print("--------------------------------")


# main agent
triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request. if no language found handoff to chinese agent",
    model="gemini-2.0-flash",
    handoffs=[
        handoff(
            agent=urdu_agent,
            on_handoff=lambda ctx: Handoff_ka_kaam(urdu_agent, ctx),
            is_enabled=False,
        ),
        handoff(
            agent=chinese_agent,
            tool_name_override="China_ka_agent",
            tool_description_override="China ke agent ko handoff karo",
            on_handoff=lambda ctx, input: Handoff_ka_kaam(chinese_agent, ctx),
            input_type=validate_chinese,
            input_filter=lambda input: (
                input
                if not input.input_history == ""
                else "please provide valid input string"
            ),
        ),
        handoff(agent=english_agent),
    ],
)
# "السلام عليكم" for testing with urdu
# "hello" for testing with english
# "Nǐ hǎo" for testing with chinese

input = input("say something in your language: ")
result = Runner.run_sync(triage_agent, input=input)
print("final output: ", result.final_output)
print("last agent: ", result.last_agent.name)

# key points:
# 1. for input_type and on_handoff
# Without input_type: on_handoff takes 1 argument (context only)
# With input_type: on_handoff takes 2 arguments (context and input)
# 2. for input_filter
# print the input param to find out what is coming and then work accordingly
# 3. for is_enabled
# hide handoff agent from LLM at run time if false
