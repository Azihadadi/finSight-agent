import json
from .state import AgentState
from .model import model_react, tools_by_name
from langchain_core.messages import ToolMessage

def tool_node(state: AgentState):
    outputs = []
    for tool_call in state["messages"][-1].tool_calls:
        tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
        outputs.append(
            ToolMessage(
                content=json.dumps(tool_result),
                name=tool_call["name"],
                tool_call_id=tool_call["id"],
            )
        )
    return {"messages": outputs}

def call_model(state: AgentState):
    response = model_react.invoke({"scratch_pad": state["messages"]})
    return {"messages": [response]}
