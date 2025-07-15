from schemas import State

def router(state:State):
    tool_needed = state.get("tool_needed","none") #assuming the identifier has set this
    if tool_needed == "get_coords":
        return {"next":"get_coords"}
    elif tool_needed == "get_rect":
        return {"next":"get_rect"}
    elif tool_needed == "get_screensize":
        return {"next":"get_screensize"}
    
    return {"next":"none"}