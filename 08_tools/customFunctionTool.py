from pydantic import BaseModel
from agents import (
    FunctionTool,
    Agent,
    Runner,
    enable_verbose_stdout_logging,
    SQLiteSession,
)
from my_config import config


def do_some_work(data: str) -> str:
    return f"{data} is done ✅"


class FunctionArgs(BaseModel):
    username: str
    age: int


async def run_function(ctx, args: str) -> str:
    parsed = FunctionArgs.model_validate_json(args)
    return do_some_work(data=f"{parsed.username} is {parsed.age} years old")


session = SQLiteSession("id123")
tool = FunctionTool(
    name="process_user",
    description="Processes extracted user data",
    params_json_schema=FunctionArgs.model_json_schema(),
    on_invoke_tool=run_function,
    # strict_json_schema=True, #required parameters can be not sent to tool if False
    # is_enabled=False,
)

agent = Agent(
    name="Process_User_Agent",
    instructions="you ask user to enter their name and age to process data using tool process_user",
    tools=[tool],
)

enable_verbose_stdout_logging()

"""Run the interactive loop within a single event loop"""
while True:
    user_input = input("Enter your input: ")
    if user_input.lower() == "exit":
        break
    result = Runner.run_sync(agent, user_input, run_config=config, session=session)
    print("Final output:", result.final_output)


# print("FunctionArgs: ", FunctionArgs)
# print("FunctionArgs.model_json_schema: ", FunctionArgs.model_json_schema())
