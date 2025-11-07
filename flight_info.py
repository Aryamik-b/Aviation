import requests
import pandas as pd
from datetime import datetime

def get_flight_by_callsign(callsign):
    """
    Fetch live flight data for a specific flight ID (callsign).
    Example: AI161, IGO512, UAE503
    """
    url = "https://opensky-network.org/api/states/all"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if not data.get("states"):
            print("❌ No flight data received from OpenSky.")
            return

        columns = [
            "icao24", "callsign", "origin_country", "time_position",
            "last_contact", "longitude", "latitude", "baro_altitude",
            "on_ground", "velocity", "true_track", "vertical_rate",
            "sensors", "geo_altitude", "squawk", "spi", "position_source"
        ]

        df = pd.DataFrame(data["states"], columns=columns)
        df["callsign"] = df["callsign"].astype(str).str.strip()

        # Match the entered callsign (case-insensitive)
        flight = df[df["callsign"].str.upper() == callsign.upper()]

        if flight.empty:
            print(f"✈️ No live data found for flight '{callsign}'. It may not be airborne right now.")
            return

        print(f"\n✅ Live Flight Data for '{callsign.upper()}'")
        print("-" * 70)

        for _, row in flight.iterrows():
            print(f"🕒 Last Updated: {datetime.utcfromtimestamp(row['last_contact']).strftime('%Y-%m-%d %H:%M:%S')} UTC")
            print(f"🌍 Origin Country: {row['origin_country']}")
            print(f"📍 Position: Latitude {row['latitude']}, Longitude {row['longitude']}")
            print(f"📈 Altitude: {row['baro_altitude']} meters")
            print(f"💨 Speed: {row['velocity']} m/s")
            print(f"🧭 Direction (Track): {row['true_track']}°")
            print(f"🛬 On Ground: {'Yes' if row['on_ground'] else 'No'}")
            print("-" * 70)

    except Exception as e:
        print("⚠️ Error fetching flight data:", e)


if __name__ == "__main__":
    print("🌐 Real-Time Flight Tracker (OpenSky API)\n")
    callsign = input("Enter flight ID (e.g., AI161, IGO512, UAE503): ").strip()
    get_flight_by_callsign(callsign)
