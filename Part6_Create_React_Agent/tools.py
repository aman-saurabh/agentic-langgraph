from langchain_core.tools import tool
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
import os

load_dotenv()

# -----------------------------------
# Tool 1: Multiplication
# -----------------------------------

@tool
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers.

    Use this tool when user asks multiplication questions and do not use this tool for addition or any other mathematical operations.
    """

    return a * b



# -----------------------------------
# Tool 2: Tavily Search
# -----------------------------------

search_tool = TavilySearch(
    api_key=os.getenv("TAVILY_API_KEY"),
    max_results=3
)


# Export all tools

tools = [
    multiply,
    search_tool
]