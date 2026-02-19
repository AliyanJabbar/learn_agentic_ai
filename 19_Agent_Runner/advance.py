from main import calculate_area, Agent, function_tool, Runner, config, ModelSettings


def advance():
    print("\n🎯 Example 5: Understanding Shared References")
    print("-" * 40)

    # Demonstrate shared references
    original_agent = Agent(
        name="Original",
        tools=[calculate_area],
        instructions="You are helpful.",
    )

    # Clone without new tools list
    shared_clone = original_agent.clone(
        name="SharedClone",
        instructions="You are creative.",
        # model_settings=ModelSettings(temperature=0.9)
    )

    # Add tool to original
    @function_tool
    def new_tool() -> str:
        return "I'm a new tool!"

    original_agent.tools.append(new_tool)
    original_agent.model_settings.temperature = 0.7
    # Check if clone also has the new tool
    print("Original tools:", len(original_agent.tools))
    print("Shared clone tools:", len(shared_clone.tools))

    print("-" * 40)
    print(f"original agent: {original_agent}\n\n")
    print(f"shared agent: {shared_clone}\n\n")
    result = Runner.run_sync(original_agent, "hi how are you", run_config=config)


advance()
