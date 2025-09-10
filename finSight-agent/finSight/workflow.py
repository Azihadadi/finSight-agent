from langgraph.graph import StateGraph, END
from .state import AgentState
from .nodes import call_model, tool_node

def should_continue(state: AgentState):
    last_message = state["messages"][-1]
    return "continue" if last_message.tool_calls else "end"

workflow = StateGraph(AgentState)
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)
workflow.add_edge("tools", "agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "tools",
        "end": END,
    },
)
workflow.set_entry_point("agent")
graph = workflow.compile()
