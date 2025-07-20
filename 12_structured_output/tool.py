from agents import function_tool, RunContextWrapper
from pydantic import BaseModel


class WeatherAnswer(BaseModel):
    location: str
    temperature_c: int
    summary: str
    details: str


# @function_tool
# def fetch_weather(wrapper: RunContextWrapper[WeatherAnswer]) -> WeatherAnswer:
#     print("weather tool running...")
#     wrapper.context.location


@function_tool
def fetch_location(wrapper: RunContextWrapper[WeatherAnswer]):
    print("location tool running...")
    # wrapper.context.location
    return wrapper.context.location
