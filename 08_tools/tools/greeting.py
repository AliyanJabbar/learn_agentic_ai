from agents import function_tool


@function_tool(name_override="greet_kro")
async def greeting_kro(name: str) -> str:
    print("greeting running...")
    return f"{name}!"
