import os
from dotenv import load_dotenv
from graph import build_graph

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

graph = build_graph()

def run_chatbot():
    state = {"messages":[], "tool_needed": None}
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            break

        state["messages"].append({"role": "user", "content": user_input})
        state = graph.invoke(state)

        last_msg = state["messages"][-1]
        print(f"ENAR: {last_msg.content}")

if __name__ == "__main__":
    run_chatbot()