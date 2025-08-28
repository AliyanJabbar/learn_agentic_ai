import asyncio
from dataclasses import dataclass
from agents import Agent, Runner, function_tool, RunContextWrapper, set_tracing_disabled
from my_config import external_model


@dataclass
class UserContext:
    username: str
    email: str | None = None
    location: str | None = None


set_tracing_disabled(True)


@function_tool()
async def search(wrapper: RunContextWrapper[UserContext], query: str) -> str:
    return [
        {"name": "John Doe", "profession": "Math Tuttor", "location": "New York"},
        {"name": "Abdullah", "profession": "Math Tuttor", "location": "Karachi"},
    ]


# dynamic instructions
async def special_prompt(
    wrapper: RunContextWrapper[UserContext], agent: Agent[UserContext]
) -> str:
    print(f"\nUser: {wrapper.context},\n Agent: {agent.name}\n")
    return f"You are a math expert. User: {wrapper.context.username}, Agent: {agent.name}. Please assist with math-related queries. users location is {wrapper.context.location}."


math_agent = Agent[UserContext](
    name="search_math_tutor",
    instructions=special_prompt,
    model=external_model,
    tools=[search],
)


async def call_agent():
    # Call the agent with a specific input
    user_context = UserContext(username="Ali", location="New york")

    output = await Runner.run(
        starting_agent=math_agent,
        input="search for the best math tutor in my location",
        context=user_context,
    )
    print(f"\n\nOutput: {output.final_output}\n\n")


asyncio.run(call_agent())
