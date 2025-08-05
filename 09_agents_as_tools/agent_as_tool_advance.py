from agents import Agent, Runner, enable_verbose_stdout_logging
from my_config import config, external_model

spanish_agent = Agent(
    name="Spanish_agent",
    instructions="You translate the user's message to Spanish",
    model=external_model,
)

french_agent = Agent(
    name="French_agent",
    instructions="You translate the user's message to French",
    model=external_model,
)


# for custom output from the agent as tool
async def check_output(output) -> str:
    print("output:", output)
    if len(output.final_output) >= 10: # to test it :  translate hi how are you ? What are you doing to spanish
        return "sorry the output is too long"
    else:
        return output.final_output # to test it :  translate hi to spanish


spanish_tool = spanish_agent.as_tool(
    tool_name="translate_to_spanish",
    tool_description="Translate the user's message to Spanish",
    custom_output_extractor=check_output,
)

french_tool = french_agent.as_tool(
    tool_name="translate_to_french",
    tool_description="Translate the user's message to French",
)
orchestrator_agent = Agent(
    name="orchestrator_agent",
    instructions=(
        "You are a translation agent. You use the tools given to you to translate."
        "If asked for multiple translations, you call the relevant tools."
    ),
    tools=[spanish_tool, french_tool],
)


def agent_as_tool(input: str):
    # enable_verbose_stdout_logging()
    result = Runner.run_sync(
        orchestrator_agent,
        input=input,
        run_config=config,
        # max_turns=2,
    )
    print(result.final_output)


def run_interactive():
    """Run the interactive loop within a single event loop"""
    while True:
        user_input = input("Enter your input: ")
        if user_input.lower() == "exit":
            break
        agent_as_tool(user_input)


run_interactive()


# for testing purpose -> to customize agent.as_tool we use agent and runner inside a function tool decorator and set max_turns in the Runner.


# from agents import Agent, Runner, enable_verbose_stdout_logging, function_tool
# from my_config import config
# import asyncio


# @function_tool
# async def run_my_math_agent() -> str:
#     """A tool that runs the math agent"""

#     agent = Agent(name="MathAgent", instructions="Math Agent")

#     result = await Runner.run(
#         agent, input="what is 2+2", max_turns=0, run_config=config
#     )

#     return str(result.final_output)


# async def testing():
#     enable_verbose_stdout_logging()
#     agent = Agent("testing_agent", instructions="testing agent", tools=[run_my_math_agent])
#     result = await Runner.run(agent, input="run math tool", run_config=config)
#     print(result.final_output)


# asyncio.run(testing())
