from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import tool
import os

os.environ["TAVILY_API_KEY"] = "YOUR_TAVILY_API_KEY"

search = TavilySearchResults()

@tool
def search_tool(query: str):
    return search.invoke(query)

@tool
def stock_advisor(stock_symbol: str) -> str:
    stock_symbol = stock_symbol.upper()
    sample_recommendations = {
        "AAPL": "Apple seems stable; consider holding or buying a small amount.",
        "TSLA": "Tesla is volatile; suitable for risk-tolerant investors.",
        "AMZN": "Amazon has growth potential; consider long-term investment.",
    }
    return sample_recommendations.get(stock_symbol, "No recommendation available for this stock.")
