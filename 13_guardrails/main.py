from pydantic import BaseModel
from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    OutputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    input_guardrail,
    output_guardrail,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    RunConfig,
)
import os
from dotenv import load_dotenv


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")


# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError(
        "GEMINI_API_KEY is not set. Please ensure it is defined in your .env file."
    )


# Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

external_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", openai_client=external_client
)

configuration = RunConfig(
    model=external_model, model_provider=external_client, tracing_disabled=True
)


# input guardrail
class MathHomeworkOutput(BaseModel):
    is_math_homework: bool
    reasoning: str


guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking you to do their math homework.",
    output_type=MathHomeworkOutput,
)


@input_guardrail
async def math_guardrail(
    wrapper: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    result = await Runner.run(
        guardrail_agent, input, context=wrapper.context, run_config=configuration
    )
    print("output of guardrail agent", result.final_output)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        # tripwire_triggered=False #result.final_output.is_math_homework,
        tripwire_triggered=result.final_output.is_math_homework,  # if the question is related to math homework then tripwire should be trigerred
    )


agent = Agent(
    name="Customer support agent",
    instructions="You are a customer support agent. You help customers with their questions.",
    input_guardrails=[math_guardrail],
)


# 1st example - This should trip the guardrail

try:
    result = Runner.run_sync(
        agent,
        "Hello, can you help me solve for x: 2x + 3 = 11?",  # related to math homework
        run_config=configuration,
    )
    print(
        "Guardrail didn't trip - the user's question is not related to maths homework"
    )
    print(result.final_output)

except InputGuardrailTripwireTriggered:
    print(
        "Math homework guardrail tripped - The user is asking to do their math homework."
    )


# 2nd example - This should not trip the guardrail
try:
    result = Runner.run_sync(agent, "Hello", run_config=configuration)
    print(result.final_output)

except InputGuardrailTripwireTriggered:
    print("Math homework guardrail tripped")


# output gurdrail


class MessageOutput(BaseModel):
    response: str


class MathOutput(BaseModel):
    is_math: bool
    reasoning: str


guardrail_agent2 = Agent(
    name="Guardrail check",
    instructions="Check if the output includes any math.",
    output_type=MathOutput,
)


@output_guardrail
async def math_guardrail2(
    wrapper: RunContextWrapper, agent: Agent, output: MessageOutput
) -> GuardrailFunctionOutput:
    result = await Runner.run(
        guardrail_agent2,
        output.response,
        context=wrapper.context,
        run_config=configuration,
    )
    print("output guardrail result : ", result.final_output)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_math,
    )


agent2 = Agent(
    name="Customer support agent",
    instructions="You are a customer support agent. You help customers with their questions.",
    output_guardrails=[math_guardrail2],
    output_type=MessageOutput,
)


# 1st example - This should trip the guardrail
try:
    Runner.run_sync(
        agent2,
        "Hello, can you help me solve for x: 2x + 3 = 11?",  # question is related to math but we don't want it
        run_config=configuration,
    )
    print("Guardrail didn't trip - means question is not related to maths homework")

except OutputGuardrailTripwireTriggered:
    print("Math output guardrail tripped")

# 2nd example - This should not trip the guardrail
try:
    Runner.run_sync(
        agent2,
        "Hello, how are you !",  # question is not related to math, so we'll continue
        run_config=configuration,
    )
    print("Guardrail didn't trip - means question is not related to maths homework")

except OutputGuardrailTripwireTriggered:
    print("Math output guardrail tripped")
