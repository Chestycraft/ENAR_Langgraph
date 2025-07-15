from typing import Annotated, TypedDict, Optional, Literal
from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field

#typedicts=======================================================================
class State(TypedDict):
    messages: Annotated[list, add_messages]                         #prompting
    tool_needed: Optional[Literal["none", "get_coords", "get_rect", "get_screensize"]]#followups
    description:Optional[str]                                       #intent
    imports:Optional[str]                                           #imports
    code:Optional[str]                                              #code
#================================================================================

#BaseModels======================================================================
class tn_identifier(BaseModel):
    tool_needed: Literal["none", "get_coords", "get_rect", "get_screensize"] = Field(
        ...,
        description="identify if user's request is not specific or lacks required details or requests something that needs a tool(e.g., coordinates or area, screensize). Use 'none' if the user was specific."
    )
    description: str = Field(..., description="explanation")
#================================================================================
