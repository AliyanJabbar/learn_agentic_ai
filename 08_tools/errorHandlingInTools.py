# Handling errors in function tools
from agents import Agent, Runner, enable_verbose_stdout_logging, function_tool
from my_config import config
import asyncio


def my_custom_error(tool_call, error):
    print("custom error handled")
    return("Oops! Something went wrong but I handled it gracefully.")


@function_tool(failure_error_function=my_custom_error)
# @function_tool(failure_error_function=None) 
async def run_my_math_agent() -> str:
    """A tool that runs the math agent"""

    agent = Agent(name="MathAgent", instructions="Math Agent")

    result = await Runner.run(
        agent, input="what is 2+2", max_turns=0, run_config=config
    )
    # max_turns=0 cause error or agent dont have enough turns to run
    # raise TypeError("something went wrong") # cause error
    return str(result.final_output)


async def customizing_tool_agents():
    enable_verbose_stdout_logging()
    agent = Agent(
        "testing_agent", instructions="testing agent", tools=[run_my_math_agent]
    )
    result = await Runner.run(agent, input="run math tool", run_config=config)
    print(result.final_output)


asyncio.run(customizing_tool_agents())

# output : Oops! Something went wrong but I handled it gracefully. -> Custom error

# OK. I ran the math tool. The results are: None.
