from crewai.tools import tool
import requests
import os

@tool
def convert_currency(amount: float, from_curr: str, to_curr: str) -> float:
    """
    Convert currency from one to another.

    Example:
    convert_currency(1000, "INR", "USD")
    """

    api_key = os.getenv("EXCHANGE_RATE_API_KEY")

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_curr}/{to_curr}/{amount}"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("result") != "success":
            return f"Error: {data.get('error-type')}"

        return float(data["conversion_result"])

    except Exception as e:
        return f"Error: {str(e)}"