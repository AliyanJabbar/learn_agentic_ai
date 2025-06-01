# To configure the LLM Provider at the Run level:
# - Define the model using OpenAIChatCompletionsModel (or any supported model class).
# - Pass the model and client via the RunConfig object to the Runner (using the run_config parameter in Runner.run or Runner.run_sync).

# When using Run-level configuration:
# - It is generally recommended to use the synchronous Runner.run_sync() method, as Run-level config is often used in sync workflows.

# Priority when all three configurations (Agent-level, Run-level, and Global-level) are set:
# - Run-level configuration has the **highest priority**.
# - It overrides both Agent-level and Global-level configurations.
