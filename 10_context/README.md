# Two types of context are present

## 1. Local Context 
Context available locally to your code: this is data and dependencies you might need when tool functions run, during callbacks like on_handoff, in lifecycle hooks, etc.

- You create any Python object you want. A common pattern is to use a dataclass or a Pydantic object.
- You pass that object to the various run methods (e.g. Runner.run(..., context=whatever)).
- All your tool calls, lifecycle hooks etc will be passed a wrapper object, - RunContextWrapper[T], where T represents your context object type which you can access via wrapper.context.
- The most important thing to be aware of: every agent, tool function, lifecycle etc for a given agent run must use the same type of context.


You can use the context for things like:

- Contextual data for your run (e.g. things like a username/uid or other information about the user)
- Dependencies (e.g. logger objects, data fetchers, etc)
- Helper functions


## 2. Agent/LLM Context
When an LLM is called, the only data it can see is from the conversation history. This means that if you want to make some new data available to the LLM, you must do it in a way that makes it available in that history. There are a few ways to do this:

- You can add it to the Agent instructions. This is also known as a "system prompt" or "developer message". System prompts can be static strings, or they can be dynamic functions that receive the context and output a string. This is a common tactic for information that is always useful (for example, the user's name or the current date).
- Add it to the input when calling the Runner.run functions. This is similar to the instructions tactic, but allows you to have messages that are lower in the chain of command.
- Expose it via function tools. This is useful for on-demand context - the LLM decides when it needs some data, and can call the tool to fetch that data.
- Use retrieval or web search. These are special tools that are able to fetch relevant data from files or databases (retrieval), or from the web (web search). This is useful for "grounding" the response in relevant contextual data.