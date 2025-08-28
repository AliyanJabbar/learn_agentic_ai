from agents import Agent, Runner, function_tool, RunContextWrapper, RunHooks, trace
from my_config import config
import asyncio


class HelloRunHooks(RunHooks):

    async def on_llm_start(
        self, context: RunContextWrapper, agent: Agent, system_prompt, input_items
    ):

        print(
            f"\n\n[RunLifecycle] LLM call for agent {agent.name} starting with system prompt: {system_prompt} and input items: {input_items}\n\n"
        )

    async def on_llm_end(self, context, agent, response):
        print(
            f"\n\n[{self.lifecycle_name}] LLM call ended with response: {response}\n\n"
        )

    async def on_agent_start(self, context: RunContextWrapper, agent: Agent):
        print(
            f"\n\n[RunLifecycle] Agent {agent.name} start with context: {context}\n\n"
        )


@function_tool
def get_weather(city: str) -> str:
    """A simple function to get the weather for a user."""
    return f"The weather for {city} is sunny."


news_agent: Agent = Agent(
    name="NewsAgent",
    instructions="You are a helpful news assistant.",
)


base_agent: Agent = Agent(
    name="BaseAgent",
    instructions="You are a helpful assistant. Talk about weather and let news_agent handle the news things",
    tools=[get_weather],
    handoffs=[news_agent],
)

with trace("RunHooksWorkFlow"):
    res = Runner.run_sync(
        starting_agent=base_agent,
        input="give one line news about gpt 5.",
        hooks=HelloRunHooks(),
        run_config=config,
    )

print(res.last_agent.name)
print(res.final_output)
hello = HelloRunHooks()
# Now check the trace in openai dashboard


asyncio.run(hello.on_llm_start(None, base_agent, "hello", "world")) #inforcing the llm call hook
