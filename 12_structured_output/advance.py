# using function_tool with structured output -> output_type don't run with function_tool in agent. Any one can run only


# 1st example
from pydantic import BaseModel
from agents import Agent, Runner, set_tracing_disabled, function_tool, SQLiteSession
from my_config import external_model
import asyncio
from tool import WeatherAnswer, fetch_location


async def advance():
    session = SQLiteSession("session_123")
    set_tracing_disabled(True)

    weather = WeatherAnswer(
        location="karachi",
        temperature_c=20,
        summary="weather is good",
        details="weather ki details",
    )
    agent = Agent(
        name="StructuredWeatherAgent",
        instructions="return the current weather with structured data",
        # tools=[fetch_weather, fetch_location],
        tools=[fetch_location],
        # output_type=WeatherAnswer,
        model=external_model,
    )

    # while True:
    res = await Runner.run(
        # agent, f"What's the temperature in {user_input}?", session=session
        agent,
        "What's the location?",
        session=session,
        context=weather,
    )
    print("type of output: ", type(res.final_output))
    print("final output: ", (res.final_output))


asyncio.run(advance())


# 2nd example
from pydantic import BaseModel
from agents import Agent, Runner, function_tool
from my_config import external_model


class TimeInfo(BaseModel):
    hours: int
    minutes: int


@function_tool
def get_time() -> TimeInfo:
    print("tool running...")
    hours = 12
    minutes = 40
    return {"hours": hours, "minutes": minutes}


model = external_model
agent = Agent(
    name="TimeAgent",
    instructions="Return the current time using the tool",
    output_type=TimeInfo,
    # tools=[get_time],
    model=model,
)

result = Runner.run_sync(agent, "What time is it?")
print(result.final_output)  # A validated TimeInfo instance
