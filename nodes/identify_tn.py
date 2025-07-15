from schemas import tn_identifier, State
from llm import llm

def identify_tn(state:State):
    last_message = state["messages"][-1]
    identifier_llm = llm.with_structured_output(tn_identifier, method="function_calling")

    result = identifier_llm.invoke([
       { "role":"system",
        "content":"""
        youre a desktop assistant for task automating youre connected to a bigger system
        youre a python smart assistant that knows what specifications actions needs
        to help the system have a better understanding of the user's request
        your job is to identify if the user's prompt needs more details or needs tools use these tools to follow them up:
        - "get_coords" →use this if user asked a task that needs coordinates like clicks but didnt provide them.
        - "get_rect" → use this if user asked a task that needs rectangle but didnt provide coordinates of the rectangle.
        - "get_screensize" → use this for identifying screensize.
        - "none" → use this if user's request is complete
        """ },
        { "role":"user", "content": last_message.content }
    ])
    return {"tool_needed": result.tool_needed, "description": result.description}