import asyncio
from pydantic import BaseModel
from agents import Agent, RunContextWrapper, Runner, function_tool
from utils.configuration import get_model


class UserInfo1(BaseModel):
    name: str
    uid: int
    location: str = "Pakistan"


@function_tool
async def fetch_user_name(wrapper: RunContextWrapper[UserInfo1]) -> str:
    """Returns the name of the user."""
    return f"User's name is {wrapper.context.name}"


@function_tool
async def fetch_user_age(wrapper: RunContextWrapper[UserInfo1]) -> str:
    """Returns the age of the user."""
    return f"User {wrapper.context.name} is 30 years old"


@function_tool
async def fetch_user_location(wrapper: RunContextWrapper[UserInfo1]) -> str:
    """Returns the location of the user."""
    return f"User {wrapper.context.name} is from {wrapper.context.location}"


@function_tool
async def set_user_location(
    wrapper: RunContextWrapper[UserInfo1], user_location: str
) -> str:
    """sets the location of the user."""
    wrapper.context.location = user_location
    return f"User's location is set to {wrapper.context.location}"


@function_tool
async def fetch_user_id(wrapper: RunContextWrapper[UserInfo1]) -> str:
    """Returns the uid of the user."""
    return f"User {wrapper.context.name} is having uid: {wrapper.context.uid}"


@function_tool
async def set_user_id(wrapper: RunContextWrapper[UserInfo1], userUid: int) -> str:
    """set the uid of the user."""
    wrapper.context.uid = userUid
    return f"user's uid is updated to {wrapper.context.uid}"


@function_tool
async def set_user_name(wrapper: RunContextWrapper[UserInfo1], user_name) -> str:
    """set the user name in the context."""
    wrapper.context.name = user_name
    return f"UserName set to {wrapper.context.name}"


user_info = UserInfo1(name="User1", uid=123)


async def main():

    agent = Agent[UserInfo1](
        name="Assistant",
        instructions="first get the name of the user and set it using set_user_name tool (only get it one time). then continue the conversation and repond the user by using tools if possible.",  # explicityly defining the name of the tool for the agent context
        tools=[
            set_user_name,
            fetch_user_name,
            fetch_user_age,
            fetch_user_location,
            set_user_location,
            fetch_user_id,
            set_user_id,
        ],
        model=get_model(),
    )

    user_input = input("enter message: ")
    result = await Runner.run(
        starting_agent=agent,
        input=user_input,
        context=user_info,
    )

    print("final output : ", result.final_output)
    print("final user_info : ", user_info)


if __name__ == "__main__":
    while True:
        asyncio.run(main())


# key points:
# agent can only remember history passed via Runner class in run in the input param or the instructions passes via agent's instructions.
# the alernative approach is to user function_tool and pass it in the agent so that the agent will decide weather to use the tool or not.
