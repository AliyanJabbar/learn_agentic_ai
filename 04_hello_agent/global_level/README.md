# To configure the LLM Provider at the Global level:
# - Use set_default_openai_api("chat_completions") to set the default API endpoint.
# - Use set_default_openai_client() to set the default client (e.g., an external AsyncOpenAI client configured with the desired model and API key).

# When using Global-level configuration:
# - Always use the synchronous Runner.run_sync() method to avoid conflicts with the event loop.

# Priority when all three configurations (Agent-level, Run-level, and Global-level) are set:
# - Global-level configuration has the **lowest priority**.
# - It is only used when no Run-level or Agent-level configuration is provided.
