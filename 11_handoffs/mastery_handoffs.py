from agents import (
    Agent,
    Runner,
    RunContextWrapper,
    handoff,
    # enable_verbose_stdout_logging,
    trace,
)
from pydantic import BaseModel
from my_config import config

# enable_verbose_stdout_logging()  # shows that at firt the agent has 3 handoffs. Each handoff agent is treated as tools with name = transfer_to_"agent_name". then the agent decides to transfer to which agent and then the response is generated.


# ---------------------------- main content starts here ----------------------------

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


# def input_ka_filter(input):
#     # print(f"input filtered: {input}")
#     main_input: list = input.input_history.split(" ")
#     if len(main_input) >= 1:
#         return input
#     else:
#         return "please provide smaller input string"


def input_ka_filter(input):
    # input is usually a RunInput object
    # You can inspect it with print(type(input), input.dict()) if needed
    if not input.input_history or input.input_history.strip() == "":
        # If input is empty or invalid → block handoff
        # input.input_history = "please provide valid input string"
        print("input is empty")
        return input

    # If valid → either return as-is or transform before passing on
    main_input = input.input_history.split(" ")
    if len(main_input) > 2:  # e.g., reject too-short inputs
        # input.input_history = "please provide valid input greater than 2"
        print("input is greater than 2")
        return input

    return input  # pass through


# main agent
triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request. if no language found handoff to chinese agent",
    model="gemini-2.0-flash",
    output_type=str,
    handoffs=[
        # handoff(
        #     agent=urdu_agent,
        #     on_handoff=lambda ctx: Handoff_ka_kaam(urdu_agent, ctx),
        #     is_enabled=False,
        # ),
        handoff(
            agent=chinese_agent,
            tool_name_override="China_ka_agent",
            tool_description_override="China ke agent ko handoff karo",
            on_handoff=lambda ctx, input: Handoff_ka_kaam(chinese_agent, ctx),
            input_type=validate_chinese,
            # input_filter=lambda input: (
            #     input
            #     if not input.input_history == ""
            #     else "please provide valid input string"
            # ),
            input_filter=input_ka_filter,
        ),
        # handoff(agent=english_agent),
    ],
)
# "السلام عليكم" for testing with urdu
# "hello" for testing with english
# "Nǐ hǎo" for testing with chinese

input = input("say something in your language: ")
with trace("handoffs"):

    result = Runner.run_sync(triage_agent, input=input, run_config=config)
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
