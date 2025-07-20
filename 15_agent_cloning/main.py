from agents import Agent, Runner
from my_config import config

# Original Agent
support_agent = Agent(
    name="support_agent",
    instructions="You are a helpful support agent that assists users with product issues.",
)

print("support agent: ", support_agent)
# Clone the agent with the same instructions, tools, and internal state
feedback_agent = support_agent.clone(
    name="feedback_agent",
    instructions="You are a feedback-collection agent. Ask users how their experience was.",
)
print("feedback agent: ", feedback_agent)
result = Runner.run_sync(
    feedback_agent,
    input="User: I'd like to give some feedback.",
    run_config=config,
)
response = result.final_output
print(response)
