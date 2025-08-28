from agents import (
    Agent,
    Runner,
    GuardrailFunctionOutput,
    input_guardrail,
    InputGuardrailTripwireTriggered,
    RunContextWrapper,
    trace,
    output_guardrail,
    OutputGuardrailTripwireTriggered,
)
from pydantic import BaseModel
from my_config import config


class WeatherSanitizer(BaseModel):
    weather_related: bool
    reason: str


weather_sanitizer = Agent(
    name="WeatherSanitizer",
    instructions="Check if this is a weather related query.",
    output_type=WeatherSanitizer,
)


@input_guardrail
async def weather_input_checker(ctx: RunContextWrapper, agent: Agent, input):

    # The runner will now return a dictionary, not a Pydantic object
    res = await Runner.run(weather_sanitizer, input, run_config=config)

    # print("\n[WEATHER SANITIZER RESPONSE]", res.final_output)

    # Access the dictionary key directly
    return GuardrailFunctionOutput(
        output_info="passed",
        tripwire_triggered=res.final_output.weather_related is False,
    )


@output_guardrail
def weather_response_checker(ctx: RunContextWrapper, agent: Agent, output):
    return GuardrailFunctionOutput(output_info="passed", tripwire_triggered=False)


base_agent: Agent = Agent(
    name="WeatherAgent",
    instructions="You are a helpful assistant.",
    input_guardrails=[weather_input_checker],
    output_guardrails=[weather_response_checker],
)

with trace("Guardrail"):
    try:
        res = Runner.run_sync(
            base_agent,
            "what is the weather in karachi",
            run_config=config,
        )
        print("[OUTPUT]", res.to_input_list())
    except InputGuardrailTripwireTriggered as e:
        print("Alert: Guardrail input tripwire was triggered!")
    except OutputGuardrailTripwireTriggered as e:
        print("Alert: Guardrail output tripwire was triggered!")
