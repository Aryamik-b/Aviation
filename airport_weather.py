import requests

# Replace with your actual OpenWeatherMap API key
API_KEY = "e6fe993d26b90f301d11b3ead4d19d58"

def get_airport_weather(icao_code):
    """
    Fetches live weather data for a given airport using its ICAO code.
    """
    # ICAO codes are linked to city names manually (simplified for demo)
    airport_city = {
        "VECC": "Kolkata",
        "VABB": "Mumbai",
        "VIDP": "Delhi",
        "VOBL": "Bangalore",
        "VOMM": "Chennai",
        "VEBS": "Bhubaneswar"
    }

    city = airport_city.get(icao_code.upper())
    if not city:
        print("Sorry, airport not in database.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print("Error fetching weather data:", data["message"])
            return

        # Extract useful info
        weather = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        visibility = data.get("visibility", "N/A")

        print(f"\n🌤️  Aviation Weather Report - {icao_code} ({city})")
        print("-" * 45)
        print(f"Weather: {weather}")
        print(f"Temperature: {temp} °C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Visibility: {visibility} meters")
        print("-" * 45)

    except Exception as e:
        print("Error:", e)


# Example usage
if __name__ == "__main__":
    print("✈️ Aviation Weather Fetcher")
    icao = input("Enter airport ICAO code (e.g., VECC, VABB, VIDP): ")
    get_airport_weather(icao)
