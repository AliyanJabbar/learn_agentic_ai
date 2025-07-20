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
    print("wrapper >>>>", wrapper)
    wrapper.context.name = user_name
    return f"UserName set to {wrapper.context.name}"


user_info = UserInfo1(name="User1", uid=123)
async def main():

    agent = Agent[UserInfo1](
        name="Assistant",
        instructions="first get the name of the user and set it using tools.",
        tools=[
            set_user_name,
            fetch_user_name,
            fetch_user_age,
            fetch_user_location,
            fetch_user_id,
            set_user_id
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


# async def advance():
#     # experiment by not passing context via runner but trying to get in function tool
#     agent = Agent[UserInfo1](
#         name="Assistant",
#         instructions="first get the name of the user and set it using tools.",
#         tools=[
#             set_user_name,
#             fetch_user_name,
#             fetch_user_age,
#             fetch_user_location,
#             fetch_user_id,
#             set_user_id,
#         ],
#         model=get_model(),
#     )

#     user_input = input("enter message: ")
#     result = await Runner.run(
#         starting_agent=agent,
#         input=user_input,
#         # context=user_info,
#     )

#     print("final output : ", result.final_output)
#     print("final user_info : ", user_info)


if __name__ == "__main__":
    while True:
        asyncio.run(main())
        # asyncio.run(advance())
