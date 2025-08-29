from agents import (
    Agent,
    Runner,
    function_tool,
    ModelSettings,
)
from my_config import config


@function_tool
def calculate_area(length: float, width: float) -> str:
    """Calculate the area of a rectangle."""
    area = length * width
    return f"Area = {length} × {width} = {area} square units"


def main():
    """Learn Model Settings with simple examples."""
    # 🎯 Example 1: Temperature (Creativity Control)
    print("\n❄️🔥 Temperature Settings")
    print("-" * 30)

    agent_cold = Agent(
        name="Cold Agent",
        instructions="You are a helpful assistant.",
        model_settings=ModelSettings(temperature=0.1),
    )

    agent_hot = Agent(
        name="Hot Agent",
        instructions="You are a helpful assistant.",
        model_settings=ModelSettings(temperature=1.9),
    )

    question = "Tell me about AI in 2 sentences"
    # question = "what is 5 * 5 / 6"

    print("Cold Agent (Temperature = 0.1):")
    result_cold = Runner.run_sync(agent_cold, question, run_config=config)
    print(result_cold.final_output)

    print("\nHot Agent (Temperature = 1.9):")
    result_hot = Runner.run_sync(agent_hot, question, run_config=config)
    print(result_hot.final_output)

    print("\n💡 Notice: Cold = focused, Hot = creative")
    print("📝 Note: Gemini temperature range extends to 2.0")

    # 🎯 Example 2: Tool Choice
    print("\n🔧 Tool Choice Settings")
    print("-" * 30)

    agent_auto = Agent(
        name="Auto",
        tools=[calculate_area],
        model_settings=ModelSettings(tool_choice="auto"),
    )

    agent_required = Agent(
        name="Required",
        tools=[calculate_area],
        model_settings=ModelSettings(tool_choice="required"),
    )

    agent_none = Agent(
        name="None",
        tools=[calculate_area],
        model_settings=ModelSettings(tool_choice="none"),
    )

    question = "What's the area of a 5x3 rectangle?"

    print("Auto Tool Choice:")
    result_auto = Runner.run_sync(agent_auto, question, run_config=config)
    print(result_auto.final_output)

    print("\nRequired Tool Choice:")
    result_required = Runner.run_sync(agent_required, question, run_config=config)
    print(result_required.final_output)

    print("\nNone Tool Choice:")
    result_none = Runner.run_sync(agent_none, question, run_config=config)
    print(result_none.final_output)

    print("\n💡 Notice: Auto = decides, Required = must use tool")


main()