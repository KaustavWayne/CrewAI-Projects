from crewai.tools import tool
from tavily import TavilyClient
import os

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def search_web(query: str) -> list:
    """
    Perform a SINGLE web search query to get travel information.

    Rules:
    - Use only ONE query per task
    - Combine weather, attractions, hotels, and cost
    - Keep results concise and relevant
    """

    try:
        response = client.search(query=query, max_results=5)
        results = response.get("results", [])

        formatted = []
        for r in results:
            formatted.append({
                "title": r.get("title"),
                "content": r.get("content"),
                "url": r.get("url")
            })

        return formatted

    except Exception as e:
        return [{"error": str(e)}]