# 🛫 Aviation Data Dashboard  

A simple yet powerful Python-based aviation project that combines **real-time flight tracking** and **live weather fetching** using open public APIs.  
This project demonstrates API integration, data handling with Pandas, and an interest in aviation analytics — inspired by real-world flight simulation systems like **X-Plane 12**.

---

## ✈️ Features

### 🌍 1. Real-Time Flight Tracker
- Track any **active aircraft** globally using its **callsign/flight ID** (e.g., `AI161`, `IGO512`, `UAE503`).
- Fetches **live flight data** (altitude, speed, coordinates, and direction) from the **OpenSky Network API**.
- Displays easy-to-read, real-time flight metrics directly in the console.

### 🌦️ 2. Aviation Weather Fetcher
- Fetches **live weather reports** (temperature, humidity, wind, and visibility) for airports using **OpenWeatherMap API**.
- Input the **ICAO airport code** (e.g., `VECC` for Kolkata, `VABB` for Mumbai).
- Displays data in an aviation-style METAR summary format.

---

## 🧠 Tech Stack
- **Language:** Python 3  
- **Libraries:**  
  - `requests` – For fetching API data  
  - `pandas` – For handling tabular flight data  
  - `datetime` – For timestamps  
- **APIs Used:**  
  - [OpenSky Network](https://opensky-network.org/apidoc/rest.html) – Real-time flight data  
  - [OpenWeatherMap](https://openweathermap.org/api) – Live weather data  

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/aviation-dashboard.git
   cd aviation-dashboard
