# import os
# from dotenv import load_dotenv
# from typing import cast
# import chainlit as cl
# from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
# from agents.run import RunConfig

# # Load the environment variables from the .env file
# load_dotenv()

# gemini_api_key = os.getenv("GEMINI_API_KEY")

# # Check if the API key is present; if not, raise an error
# if not gemini_api_key:
#     raise ValueError(
#         "GEMINI_API_KEY is not set. Please ensure it is defined in your .env file."
#     )


# @cl.on_chat_start
# async def start():
#     print("hi")


# @cl.on_chat_start
# async def start():
#     external_client = AsyncOpenAI(
#         api_key=gemini_api_key,
#         base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
#     )

#     external_model = OpenAIChatCompletionsModel(
#         model="gemini-2.0-flash", openai_client=external_client
#     )

#     config = RunConfig(
#         model=external_model, model_provider=external_client, tracing_disabled=True
#     )
#     """Set up the chat session when a user connects."""
#     # Initialize an empty chat history in the session.
#     cl.user_session.set("chat_history", [])

#     cl.user_session.set("config", config)
#     agent: Agent = Agent(
#         name="Assistant",
#         instructions="You are a helpful assistant",
#         model=external_model,
#     )
#     cl.user_session.set("agent", agent)

#     await cl.Message(
#         content="Welcome to the Aliyan's AI Assistant! How can I help you today?"
#     ).send()


# @cl.on_message
# async def main(message: cl.Message):
#     """Process incoming messages and generate responses."""
#     # Send a thinking message
#     msg = cl.Message(content="Thinking...")
#     await msg.send()

#     agent: Agent = cast(Agent, cl.user_session.get("agent"))
#     config: RunConfig = cast(RunConfig, cl.user_session.get("config"))

#     # getting the chat history from the session.
#     history = cl.user_session.get("chat_history") or []

#     # Append the user's message to the history.
#     history.append({"role": "user", "content": message.content})

#     try:
#         print("\n[CALLING_AGENT_WITH_CONTEXT]\n", history, "\n")
#         result = Runner.run_sync(starting_agent=agent, input=history, run_config=config)

#         response_content = result.final_output

#         # Update the thinking message with the actual response
#         msg.content = response_content
#         await msg.update()

#         # Update the session with the new history.
#         cl.user_session.set("chat_history", result.to_input_list())

#         # Log the interaction
#         print(f"User: {message.content}")
#         print(f"Assistant: {response_content}")

#     except Exception as e:
#         msg.content = f"Error: {str(e)}"
#         await msg.update()
#         print(f"Error: {str(e)}")


# simple practice code unseen
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

from dotenv import load_dotenv
import os
import chainlit as cl


@cl.on_chat_start
async def start():
    load_dotenv(".env")
    external_client = AsyncOpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    external_model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash", openai_client=external_client
    )

    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant of Aliyan Jabbar",
        model=external_model,
    )
    cl.user_session.set("chat_history", [])
    cl.user_session.set("agent", agent)


@cl.on_message
async def main(message: cl.Message):
    """Process incoming messages and generate responses."""
    msg = cl.Message(content="Thinking...")
    await msg.send()

    agent: Agent = cl.user_session.get("agent")
    history = cl.user_session.get("chat_history")
    history.append({"role": "user", "content": message.content})
    result = Runner.run_sync(starting_agent=agent, input=history)
    print("result:", result.final_output)
    msg.content = result.final_output
    await msg.update()
