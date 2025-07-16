from dotenv import load_dotenv
import os
import json
from litellm import completion
import chainlit as cl


# makig custom exception for apikey not set error
class ApiKeyNotSetError(Exception):
    """Custom exception for when the API key is not set."""

    pass


load_dotenv()  # loading variables from .env file


api_key = os.getenv("GEMEINI_API_KEY")


if not api_key:
    raise ApiKeyNotSetError(
        "GEMEINI_API_KEY is not set in the environment variables. Please set it in the .env file."
    )

# telling the agent who he is: 
agent_description = {"role":"system","content":"you are just an assistant of Aliyan Jabbar, a professional frontend developer, who is studying latest Agentic AI tenchniques and building AI agents. You are here to help him with his work means if someone asks about him or his services, you just tell him that who is Aliyan and what he offers. Aliyan Jabbar provides several services including web development, Frontend Development, UX/UI Development, AI agent development, and more. You can answer questions related to these topics and assist him in his tasks."}

# @cl.on_chat_start  # will call the function automatically when the chat starts !
async def starts():
    """Function to start the Chainlit app."""
    cl.user_session.set("chat_history", [])
    # await cl.Message("Hi, I am a personal assistant. How can I help you?").send()


@cl.on_message  # will call the function automatically when a message is sent
async def main(message):
    """Process incoming messages and generate responses."""

    msg = cl.Message(content="Thinking...")
    await msg.send()

    # getting chat history from user session of chainlit otherwise initializing it
    history = cl.user_session.get("chat_history") or [agent_description]

    # appending the user message to the chat history
    history.append({"role": "user", "content": message.content})

    try:
        response = completion(
            model="gemini/gemini-1.5-flash",
            api_key=api_key,
            messages=history,
        )

        main_response = response.choices[0].message.content
        msg.content = main_response
        await msg.update()

        history.append({"role": "assistant", "content": main_response})
        cl.user_session.set("chat_history", history)

        print(f"User: {message.content}")
        print(f"Assistant: {main_response}")
    except Exception as e:
        msg.content = f"An error occurred: {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")


@cl.on_chat_end  # will call the function automatically when the chat ends
async def end_chat():
    """Function to handle chat end."""
    with open("chat_history.json", "w") as f:
        history = cl.user_session.get("chat_history") or [agent_description]
        json.dump(history, f, indent=2)
    print("Chat history saved to chat_history.json")
    await cl.Message("Thank you for chatting!").send()