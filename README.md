# 🌦️ Weather-App

A simple desktop-based weather application built using Python and Tkinter.

Weather-App allows you to search for a city and view its current weather conditions, temperature, wind speed, atmospheric pressure, and local time.

It uses the OpenWeatherMap API to retrieve weather information and geolocation libraries to determine the local time of the searched city.

## ⚙️ Features

- **City Search:** Search for weather information by entering a city name.
- **Temperature:** Displays the current temperature in Celsius.
- **Weather Conditions:** Shows the current weather condition and description.
- **Wind Speed:** Displays the current wind speed.
- **Atmospheric Pressure:** Provides the current atmospheric pressure.
- **Local Time:** Displays the local time of the searched city.
- **Simple GUI:** A clean desktop interface built using Tkinter.

## 📥 Installation

Make sure Python is installed on your system before proceeding.

### 1. Install the required libraries

Install each dependency separately using pip.

**Geopy**
```bash
pip install geopy
```

**TimezoneFinder**
```bash
pip install timezonefinder
```

**Requests**
```bash
pip install requests
```

**Pytz**
```bash
pip install pytz
```

### 2. Tkinter

Tkinter usually comes bundled with Python.

If you are using Arch Linux, install it with:

```bash
sudo pacman -S tk
```

### 3. Set up the OpenWeatherMap API

The application uses the OpenWeatherMap API to retrieve weather information.

1. Visit [OpenWeatherMap](https://openweathermap.org/api).
2. Create an account.
3. Generate an API key.
4. Open `app.py`.
5. Add your API key:

```python
app_id = "YOUR_API_KEY"
```

**Note:** Newly generated API keys may take some time to become active.

## ✔ Running the Application

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Weather-App.git
```

Navigate into the project directory:

```bash
cd Weather-App
```

Run the application:

```bash
python app.py
```

Make sure all the required image files are present in the same directory as `app.py`.

## 📁 Project Structure

```text
Weather-App/
│
├── app.py
├── bing.png
├── searchbar.png
├── searchicon.png
├── bottombox.png
└── README.md
```

## ❗❗ Notes

- An active internet connection is required.
- A valid OpenWeatherMap API key is required.
- Keep your API key private. Avoid uploading it directly to a public GitHub repository.
- City search and timezone detection depend on external services.

## 👨‍💻 About

Weather-App started as a Python project to explore GUI development, API integration, and working with external libraries.

It combines a simple interface with real-time weather data to create a lightweight desktop application.

**Built with Python 🐍**
