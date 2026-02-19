import asyncio
from agents import Agent, Runner
from agents.run import AgentRunner, set_default_agent_runner
from my_config import config


class CustomAgentRunner(AgentRunner):
    async def run(self, starting_agent, input, **kwargs):
        # Custom preprocessing

        print(f"CustomAgentRunner.run()")
        # input = await self.preprocess(input)

        # Call parent with custom logic
        result = await super().run(starting_agent, input, **kwargs)

        # Custom postprocessing & analytics
        # await self.log_analytics(result)
        return result

set_default_agent_runner(CustomAgentRunner())


async def main():
    # This agent will use the custom LLM provider
    agent = Agent(
        name="Assistant",
        instructions="greet users with a friendly tone.",
    )
    result = await Runner.run(
        agent,
        "When I was 3 years old, my partner was 3 times my age. Now, I am 20 years old. How old is my partner?",
        run_config=config,
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
