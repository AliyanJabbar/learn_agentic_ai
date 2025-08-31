from agents import (
    Agent,
    Runner,
    function_tool,
    ModelSettings,
    trace,
    enable_verbose_stdout_logging,
)
from my_config import config


@function_tool
def weather(city: str) -> str:
    """find weather in city."""
    print("weather called")
    return f"{city} is rainy"


# top_p
def expert():
    # enable_verbose_stdout_logging()
    """Learn Model Settings with simple examples."""
    print("\n🔧 Tool Choice Settings")
    print("-" * 30)

    high_topp_agent = Agent(
        name="high_topp_agent",
        # tools=[weather],
        model_settings=ModelSettings(
            # tool_choice="nation_sports",
            # parallel_tool_calls=False,  # if true can call multiple tools in one turn or generation
            top_p=0.9  # This means more creativity and variety in the output.Responses may be less deterministic and more “open-ended.”
        ),
        # reset_tool_choice=False,
    )
    low_topp_agent = Agent(
        name="low_topp_agent",
        # tools=[weather],
        model_settings=ModelSettings(
            # tool_choice="nation_sports",
            # parallel_tool_calls=False,  # if true can call multiple tools in one turn or generation
            top_p=0.1  # This means more focused, deterministic, and repetitive responses.Less creativity, more predictable.
        ),
        # reset_tool_choice=False,
    )

    question = "What is the current situation of AI market in two lines"
    with trace("Model_Settings"):

        # print("Tool Run:")
        high = Runner.run_sync(high_topp_agent, question, run_config=config)
        low = Runner.run_sync(low_topp_agent, question, run_config=config)
        print(f"\n\nhigh: {high.final_output}\n\n")
        print(f"\n\nlow: {low.final_output}\n\n")


# frequence and presence penalty
# 
def f_p_p():
    # enable_verbose_stdout_logging()
    """Learn Model Settings with simple examples."""
    print("\n🔧 Tool Choice Settings")
    print("-" * 30)

    high_f_p_agent = Agent(
        name="high_f_p_agent",
        # model_settings=ModelSettings(frequency_penalty=0.9), #Model will try hard to use different words and avoid repeatancy.
        model_settings=ModelSettings(presence_penalty=0.9), #The model will try not to reuse words like “AI,” “market,” etc., even if they’re central to the question.
    )
    low_f_p_agent = Agent(
        name="low_f_p_agent",
        # model_settings=ModelSettings(frequency_penalty=0.1), #Model can reuse common words/phrases if it thinks they’re relevant.
        model_settings=ModelSettings(presence_penalty=0.1), #Model is free to repeat key words naturally.
    )

    question = "What is the current situation of AI market in two lines"
    with trace("Model_Settings"):

        # print("Tool Run:")
        high = Runner.run_sync(high_f_p_agent, question, run_config=config)
        low = Runner.run_sync(low_f_p_agent, question, run_config=config)
        print(f"\n\nhigh: {high.final_output}\n\n")
        print(f"\n\nlow: {low.final_output}\n\n")


f_p_p()
