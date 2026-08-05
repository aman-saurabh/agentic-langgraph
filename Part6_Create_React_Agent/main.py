# create_react_agent is deprecated now, so we are using create_agent instead in this example. 
# The new create_agent function is more flexible and allows you to create agents with different reasoning strategies, including ReAct.

from dotenv import load_dotenv
import os

load_dotenv()


from langchain_groq import ChatGroq
from langchain.agents import create_agent


from tools import tools
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage


# -----------------------------------
# Create LLM
# -----------------------------------

llm = ChatGroq(
    model=os.getenv("GROQ_MODEL_NAME"),
    temperature=0
)



# -----------------------------------
# Create ReAct Agent
# -----------------------------------

agent = create_agent(
    model=llm,
    tools=tools
)



# -----------------------------------
# Run Agent
# -----------------------------------

def ask_agent(question: str):

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        }
    )
    display_messages(response)
    return response["messages"][-1].content

def display_messages(response: dict):
    for msg in response["messages"]:

        print("\n" + "-" * 80)

        if isinstance(msg, HumanMessage):
            print(f"👤 USER: {msg.content}")

        elif isinstance(msg, AIMessage):
            print("🤖 AI")

            if msg.tool_calls:
                for tool in msg.tool_calls:
                    print(f"🔧 Tool Call : {tool['name']}")
                    print(f"📥 Arguments: {tool['args']}")
            else:
                print(f"💬 {msg.content}")

        elif isinstance(msg, ToolMessage):
            print(f"⚙️ Tool Called : {msg.name}")
            print(f"{msg.content[:200]}{'...' if len(msg.content) > 200 else ''}")


if __name__ == "__main__":

    while True:

        question = input("\nAsk: ")

        if question.lower() == "exit":
            break


        answer = ask_agent(question)

        print("\nAnswer:")
        print(answer)