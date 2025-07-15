from schemas import State
from llm import llm

def get_coords(state:State):
    print(state.get("description"))
    return print("getcoords triggered")