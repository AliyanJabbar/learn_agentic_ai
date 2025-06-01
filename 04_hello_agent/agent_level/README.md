# To configure the LLM Provider at the Agent level:
# - We define the model using OpenAIChatCompletionsModel (or any supported model class) and assign it to the Agent.
# - This allows each agent to have its own unique model and client.
# 
# When using Agent-level configuration:
# - Always use the asynchronous Runner.run() method to avoid conflicts with event loops.
# 
# Priority when all three configurations (Agent-level, Run-level, and Global-level) are set:
# - Agent-level configuration has the **second-highest** priority.
# - It is used when no Run-level configuration is provided.
