import requests
from datetime import datetime

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_ollama import ChatOllama


# ---------------------------------------------------------
# TOOL 1
# Convert a city/place name into latitude and longitude
# ---------------------------------------------------------

@tool
def find_location(city: str) -> dict:
    """
    Find the latitude and longitude of a city or location.

    Use this tool whenever the user provides a city name
    but latitude and longitude are not known.
    """

    print(f"\n[TOOL] Finding location: {city}")

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json",
    }

    response = requests.get(
        url,
        params=params,
        timeout=10,
    )

    response.raise_for_status()

    data = response.json()

    results = data.get("results", [])

    if not results:
        return {
            "error": f"Location '{city}' was not found."
        }

    place = results[0]

    result = {
        "name": place.get("name"),
        "latitude": place.get("latitude"),
        "longitude": place.get("longitude"),
        "country": place.get("country"),
        "timezone": place.get("timezone"),
    }

    print("[TOOL RESULT]", result)

    return result


# ---------------------------------------------------------
# TOOL 2
# Get hourly weather information
# ---------------------------------------------------------

@tool
def get_weather(
    latitude: float,
    longitude: float,
    date: str,
    start_hour: int,
    end_hour: int,
) -> dict:
    """
    Get the hourly weather forecast for a location.

    Args:
        latitude: Latitude of the location.
        longitude: Longitude of the location.
        date: Date in YYYY-MM-DD format.
        start_hour: Starting hour using 24-hour format.
        end_hour: Ending hour using 24-hour format.

    Example:
        date="2026-09-30"
        start_hour=14
        end_hour=17

    This represents 2 PM through 5 PM.
    """

    print(
        f"\n[TOOL] Getting weather "
        f"lat={latitude}, lon={longitude}, "
        f"date={date}, hours={start_hour}-{end_hour}"
    )

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,

        "hourly": ",".join([
            "temperature_2m",
            "apparent_temperature",
            "precipitation_probability",
            "precipitation",
            "weather_code",
            "wind_speed_10m",
            "wind_gusts_10m",
        ]),

        "timezone": "auto",

        "start_date": date,
        "end_date": date,
    }

    response = requests.get(
        url,
        params=params,
        timeout=10,
    )

    response.raise_for_status()

    data = response.json()

    hourly = data.get("hourly", {})

    times = hourly.get("time", [])

    temperatures = hourly.get(
        "temperature_2m", []
    )

    apparent_temperatures = hourly.get(
        "apparent_temperature", []
    )

    rain_probabilities = hourly.get(
        "precipitation_probability", []
    )

    precipitation = hourly.get(
        "precipitation", []
    )

    weather_codes = hourly.get(
        "weather_code", []
    )

    wind_speeds = hourly.get(
        "wind_speed_10m", []
    )

    wind_gusts = hourly.get(
        "wind_gusts_10m", []
    )

    forecast = []

    for i, time_string in enumerate(times):

        dt = datetime.fromisoformat(time_string)

        # Include:
        # 14:00
        # 15:00
        # 16:00
        # 17:00
        #
        # for start_hour=14, end_hour=17

        if start_hour <= dt.hour <= end_hour:

            forecast.append({
                "time": time_string,
                "temperature_c":
                    temperatures[i],

                "apparent_temperature_c":
                    apparent_temperatures[i],

                "precipitation_probability_percent":
                    rain_probabilities[i],

                "precipitation_mm":
                    precipitation[i],

                "weather_code":
                    weather_codes[i],

                "wind_speed_kmh":
                    wind_speeds[i],

                "wind_gusts_kmh":
                    wind_gusts[i],
            })

    result = {
        "latitude": latitude,
        "longitude": longitude,
        "timezone": data.get("timezone"),
        "date": date,
        "forecast": forecast,
    }

    print("\n[TOOL RESULT]")

    for hour in forecast:
        print(hour)

    return result


# ---------------------------------------------------------
# LOCAL LLM
# ---------------------------------------------------------

model = ChatOllama(
    model="qwen3:0.6b",
    base_url="http://localhost:11434",
    temperature=0,
)


# ---------------------------------------------------------
# AGENT
# ---------------------------------------------------------

agent = create_agent(
    model=model,

    tools=[
        find_location,
        get_weather,
    ],

    system_prompt="""
You are a sports planning assistant.

Your job is to help users decide whether outdoor
activities such as cricket are reasonable given the
weather forecast.

When the user asks about playing cricket:

1. Determine the location.

2. If only a city/place name is provided, use the
   find_location tool to obtain latitude and longitude.

3. Use get_weather to retrieve the forecast.

4. Pay particular attention to:

   - precipitation probability
   - precipitation amount
   - temperature
   - apparent temperature
   - wind speed
   - wind gusts
   - weather conditions

5. Explain the weather data before making a recommendation.

6. Weather forecasts are uncertain. Never claim that
   rain or thunderstorms are guaranteed or impossible.

7. If precipitation probability or severe weather risk
   is significant, clearly explain the risk to the user.

8. If the requested date or time is ambiguous, ask the
   user for clarification instead of inventing it.

9. Never invent weather data. Always use the weather tool
   when weather information is needed.
"""
)


# ---------------------------------------------------------
# RUN AGENT
# ---------------------------------------------------------

def ask_agent(question: str):

    print("\n==========================================")
    print("USER:", question)
    print("==========================================\n")

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question,
                }
            ]
        }
    )

    final_message = result["messages"][-1]

    print("\n==========================================")
    print("AGENT RESPONSE")
    print("==========================================\n")

    print(final_message.content)


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

if __name__ == "__main__":

    print()
    print("Cricket Weather Planning Agent")
    print("------------------------------")
    print("Type 'exit' to quit.")
    print()

    while True:

        question = input("You: ").strip()

        if question.lower() in {
            "exit",
            "quit",
            "q",
        }:
            print("Goodbye!")
            break

        if not question:
            continue

        try:
            ask_agent(question)

        except Exception as e:
            print("\nERROR:", e)
