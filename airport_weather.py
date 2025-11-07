# -*- coding: utf-8 -*-
# Aviation Weather Fetcher (OpenWeatherMap) – enter ICAO (e.g., VECC)

import requests

# 🔑 Put your OpenWeatherMap API key here
API_KEY = "e6fe993d26b90f301d11b3ead4d19d58"

# Clean ICAO -> City mapping (India + a few big international hubs)
airport_city = {
    # --- India (major) ---
    "VECC": "Kolkata",
    "VIDP": "New Delhi",
    "VABB": "Mumbai",
    "VOBL": "Bengaluru",
    "VOMM": "Chennai",
    "VOHS": "Hyderabad",
    "VAAH": "Ahmedabad",
    "VAPO": "Pune",
    "VOTV": "Thiruvananthapuram",
    "VAGO": "Goa",
    "VILK": "Lucknow",
    "VICG": "Chandigarh",
    "VANP": "Nagpur",
    "VOTP": "Tirupati",
    "VABP": "Bhopal",
    "VOCI": "Kochi",
    "VEPT": "Patna",
    "VOBG": "HAL Bengaluru",
    "VEAT": "Agartala",
    "VEGT": "Guwahati",
    "VOTR": "Tiruchirappalli",
    "VOTN": "Madurai",
    "VOML": "Mangaluru",
    "VABV": "Vadodara",
    "VAPR": "Porbandar",
    "VAJB": "Jabalpur",
    "VAAU": "Aurangabad",
    "VOTK": "Tuticorin",
    "VOPC": "Puducherry",
    "VILH": "Leh",
    "VISR": "Srinagar",
    "VIAR": "Amritsar",
    "VIGG": "Kullu",
    "VIKG": "Kangra",
    "VIBR": "Bareilly",
    "VIPT": "Pantnagar",
    "VEMN": "Dimapur",
    "VEGY": "Gaya",
    "VEJT": "Jorhat",
    "VERC": "Ranchi",
    "VEIM": "Imphal",
    "VEBS": "Bhubaneswar",
    "VABJ": "Bhuj",
    "VAND": "Nanded",
    "VOBZ": "Bellary",
    "VOPB": "Port Blair",
    "VAID": "Indore",
    "VAUD": "Udaipur",
    "VABM": "Belagavi",
    "VAJM": "Jamnagar",
    "VOCL": "Calicut",
    "VOHB": "Hubballi",
    "VEBD": "Bagdogra",
    "VEPY": "Pakyong",
    # --- International hubs (handy for testing) ---
    "OMDB": "Dubai",
    "OTHH": "Doha",
    "EGLL": "London",
    "LFPG": "Paris",
    "EDDF": "Frankfurt",
    "RJTT": "Tokyo",
    "KLAX": "Los Angeles",
    "KJFK": "New York",
    "WSSS": "Singapore",
    "ZBAA": "Beijing"
}

def get_airport_weather(icao_code: str) -> None:
    """
    Fetches current weather for the city mapped from an ICAO code.
    Uses OpenWeatherMap Current Weather API (metric units).
    """
    if not API_KEY or API_KEY == "YOUR_OPENWEATHERMAP_API_KEY":
        print("⚠️ Please set your OpenWeatherMap API key in API_KEY.")
        return

    city = airport_city.get(icao_code.upper())
    if not city:
        print("⚠️ Unknown ICAO code. Please check and try again.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        resp = requests.get(url, timeout=12)
        data = resp.json()
    except Exception as e:
        print("⚠️ Network/API error while contacting OpenWeatherMap:", e)
        return

    if data.get("cod") != 200:
        print("❌ Error fetching weather data:", data.get("message", "Unknown error"))
        return

    weather = data["weather"][0]["description"].title()
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"].get("speed", "N/A")
    visibility = data.get("visibility", "N/A")

    print(f"\n🌤️  Aviation Weather Report - {icao_code.upper()} ({city})")
    print("-" * 50)
    print(f"Weather: {weather}")
    print(f"Temperature: {temp} °C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Visibility: {visibility} meters")
    print("-" * 50)

if __name__ == "__main__":
    print("🌦️ Aviation Weather Fetcher (OpenWeatherMap)\n")
    code = input("Enter airport ICAO code (e.g., VECC, VABB, OMDB): ").strip()
    get_airport_weather(code)
