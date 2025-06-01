# Configuration of LLM Providers (with OpenAI Agents SDK + other models like Gemini)
# There are three ways to configure the model and client:

# 1. Agent Level -> Every agent uses its own configured model (preferred in most cases) {async-friendly}
# 2. Run Level -> The model is configured per run, affecting all agents in that run (highest priority) {sync or async}
# 3. Global Level -> The default model is applied to all agents if not specified otherwise (lowest priority) {sync-friendly}

# Priority when all three levels are configured (agent, run, global):
# 1. Run Level -> Overrides agent and global; model is chosen for each run
# 2. Agent Level -> Model is tied to the agent itself; used when run-level is not specified
# 3. Global Level -> Fallback model if neither run-level nor agent-level is provided
