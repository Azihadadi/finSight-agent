# finSight-agent

**FinSight-agent** is an AI-powered financial assistant built using **ReAct agent architecture** with **LangGraph**. It integrates real-time search capabilities and stock investment advising to help users make informed decisions.

---

## Features

- **ReAct Agent Architecture**: Implements the Reason + Act loop for step-by-step problem solving.
- **Tool Integration**: Uses multiple tools to fetch data and provide actionable recommendations.
- **Interactive Workflow**: Conditional edges determine whether the agent should continue fetching tools or finalize the response.
- **Extensible Design**: Easy to add new tools or connect to live APIs for real-time data.
- **End-to-End Demo**: A single notebook (`notebooks/finSight-agent.ipynb`) contains the full demo for experimentation and testing.

---

## Tools

| Tool | Purpose | Input | Output |
|------|---------|-------|--------|
| **Search Tool** | Fetches up-to-date information from the web via Tavily API | Query string | Search results text |
| **Stock Advisor Tool** | Provides investment recommendations based on stock symbols | Stock ticker symbol (e.g., AAPL) | Recommendation text |

> Both tools can be enhanced to use real-time APIs for more accurate and dynamic results.

---

## Architecture

1. **User Query** → Added to AgentState  
2. **Model Node (`call_model`)** → Generates reasoning and tool calls  
3. **Tool Node (`tool_node`)** → Executes tool calls and updates state  
4. **Conditional Edges (`should_continue`)** → Determines whether to continue using tools or finish  
5. **Final Response** → Aggregates reasoning and tool results for the user  

> This architecture ensures step-by-step reasoning and dynamic tool usage.

---

## Getting Started

### Requirements

Install dependencies using the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```
Or in Colab:
```bash
!pip install -U langgraph langchain-openai
!pip install langgraph==0.3.34 langchain-openai==0.3.14 langchainhub==0.1.21 langchain==0.3.24 pygraphviz==1.14 langchain-community==0.3.23
```
### Running the Notebook

Open the notebook in Colab
```bash
notebooks/finSight-agent.ipynb
```
Run the cells step by step. Example query already included in the notebook:
```bash
inputs = {"messages": [HumanMessage(content="Can you check the latest news about Tesla stock and then tell me if it's a good investment?")]}
```
- The agent will first fetch search results and then provide a stock recommendation.
- Demonstrates step-by-step reasoning with tool usage

---

## Future Improvements
- Connect tools to live stock APIs for real-time data
- Add historical stock analysis and trend predictions
- Develop a React frontend for interactive user experience
- Include unit tests for workflow nodes and tools
  
---

## Repository Structure
```
finSight-agent/
├── notebooks/         # Full notebook
│   └── finSight-agent.ipynb
├── requirements.txt
└── README.md

```

---

## Why FinSight-agent?
- Demonstrates advanced AI agent design with LangGraph
- Integrates multiple tools for real-world financial applications
- Provides a clear step-by-step reasoning process, which is key for transparency and reliability
- Ready for extension
