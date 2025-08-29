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


@function_tool
def nation_sports(country: str) -> str:
    """find name of the city."""
    print("sports called")
    return f"{country} has cricket"


def main():
    # enable_verbose_stdout_logging()
    """Learn Model Settings with simple examples."""
    print("\n🔧 Tool Choice Settings")
    print("-" * 30)

    agent = Agent(
        name="Agent",
        tools=[weather, nation_sports],
        model_settings=ModelSettings(
            tool_choice="nation_sports",
            parallel_tool_calls=False,  # if true can call multiple tools in one turn or generation
        ),
        # reset_tool_choice=False,
    )

    question = "What's the weather in karachi?"
    with trace("Model_Settings"):

        print("Tool Run:")
        result_auto = Runner.run_sync(agent, question, run_config=config)
        print(result_auto.final_output)


main()
