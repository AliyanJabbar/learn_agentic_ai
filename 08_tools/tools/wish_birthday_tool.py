from agents import function_tool


@function_tool("wish_birthday")
async def wish_birthday(name: str, age: int) -> str:
    """
    A tool to wish someone a happy birthday.

    Args:
        name (str): The name of the person.
        age (int): The age of the person.

    Returns:
        str: A birthday wish message.
    """
    return f"Happy {age}th Birthday, {name}! 🎉🎂"