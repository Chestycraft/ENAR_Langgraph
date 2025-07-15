from langgraph.graph import StateGraph, START, END
from schemas import State
from nodes.identify_tn import identify_tn
from nodes.router import router
from nodes.get_coords import get_coords
from nodes.get_rect import get_rect
from nodes.get_screensize import get_screensize

def build_graph():
    gb = StateGraph(State)#make the state graph with schema defined from State

    gb.add_node("identify_tn", identify_tn)# the identify function
    gb.add_node("router", router)
    gb.add_node("get_coords", get_coords)
    gb.add_node("get_rect", get_rect)
    gb.add_node("get_screensize", get_screensize)

    gb.add_edge(START, "identify_tn")
    gb.add_edge("identify_tn", "router")

    gb.add_conditional_edges(
        "router", 
        lambda state: state.get("next"),#assuming the identify_tn has set this
        {"get_coords": "get_coords", "get_rect": "get_rect","get_screensize": "get_screensize", "none": END}
        )

    gb.add_edge("get_coords", END)
    gb.add_edge("get_rect", END)
    gb.add_edge("get_screensize", END)

    return gb.compile()