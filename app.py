
import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Photon
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


# ---------------- WEATHER APPLICATION ---------------- #

root = tk.Tk()
root.title("B . A . S . I . X")
root.geometry("900x500+300+200")
root.resizable(False, False)
root.configure(bg="#FFFFFF")

appicon = tk.PhotoImage(file="bing.png")
root.iconphoto(False, appicon)


def getweather():

    try:
        city = srcbox.get().strip()

        if not city:
            messagebox.showwarning("Input Error", "Enter a city name")
            return

        # Get geographical location
        geolocator = Photon(user_agent="basix_weather")
        location = geolocator.geocode(city)

        if location is None:
            messagebox.showerror("Error", "City not found")
            return

        # Get timezone
        obj = TimezoneFinder()
        result = obj.timezone_at(
            lng=location.longitude,
            lat=location.latitude
        )

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")

        clock.config(text=current_time)

        # OpenWeatherMap API
        app_id = "5b4c3b4006aea0395d44d8b0618d65f9"

        api = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={app_id}"
        )

        response = requests.get(api, timeout=10)
        response.raise_for_status()

        json_data = response.json()

        # Extract weather information
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']

        temp = round(json_data['main']['temp'] - 273.15, 1)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind_speed = json_data['wind']['speed']

        # Update GUI
        temp_box.config(text=f"{temp}°C")
        elab.config(text=condition)

        wind_box.config(text=f"{wind_speed} m/s")
        moreinfo_box.config(text=description)
        pressure_box.config(text=f"{pressure} hPa")

    except requests.exceptions.RequestException:
        messagebox.showerror("API Error", "Unable to retrieve weather data")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- GUI ELEMENTS ---------------- #

srcbar = tk.PhotoImage(file="searchbar.png")
img_bar = tk.Label(root, image=srcbar, border=0)
img_bar.place(x=10, y=10)

srcbox = tk.Entry(
    root,
    width=14,
    border=0,
    justify="center",
    font=("bahnschrift", 25),
    bg="#F0F0F0",
    fg="#000000"
)
srcbox.place(x=40, y=13)

srcicon = tk.PhotoImage(file="searchicon.png")
img_icon = tk.Button(
    root,
    image=srcicon,
    borderwidth=0,
    cursor="hand2",
    bg="#F0F0F0",
    command=getweather
)
img_icon.place(x=300, y=15)

s = tk.PhotoImage(file="bottombox.png")
l = tk.Label(root, image=s, border=0)
l.place(x=10, y=380)


# Bottom information labels

wind = tk.Label(
    root, text="Wind",
    font=("bahnschrift", 20, "bold"),
    fg="#FFFFFF", bg="#2A2A2A"
)
wind.place(x=70, y=385)

info = tk.Label(
    root, text="More Info",
    font=("bahnschrift", 20, "bold"),
    fg="#FFFFFF", bg="#2A2A2A"
)
info.place(x=370, y=385)

pressure = tk.Label(
    root, text="Pressure",
    font=("bahnschrift", 20, "bold"),
    fg="#FFFFFF", bg="#2A2A2A"
)
pressure.place(x=725, y=385)


# Clock

clock = tk.Label(
    root,
    font=("bahnschrift", 20),
    bg="#FFFFFF"
)
clock.place(x=770, y=10)

clock_text = tk.Label(
    root,
    text="C U R R E N T   T I M E",
    font=("bahnschrift", 6, "bold"),
    bg="#2A2A2A",
    fg="#FFFFFF"
)
clock_text.place(x=780, y=50)


# Temperature

temp_box = tk.Label(
    root,
    font=("bahnschrift", 70, "bold"),
    fg="#2A2A2A",
    bg="#FFFFFF"
)
temp_box.place(x=400, y=150)

elab = tk.Label(
    root,
    font=("bahnschrift", 15, "bold"),
    fg="#2A2A2A",
    bg="#FFFFFF"
)
elab.place(x=410, y=260)


# Weather information

wind_box = tk.Label(
    root, text="_ . _",
    font=("bahnschrift", 15, "bold"),
    justify="center",
    bg="#2A2A2A",
    fg="#FFFFFF"
)
wind_box.place(x=80, y=435)

moreinfo_box = tk.Label(
    root, text="_ . _",
    font=("bahnschrift", 15),
    bg="#2A2A2A",
    fg="#FFFFFF"
)
moreinfo_box.place(x=410, y=435)

pressure_box = tk.Label(
    root, text="_ . _",
    font=("bahnschrift", 15, "bold"),
    justify="center",
    bg="#2A2A2A",
    fg="#FFFFFF"
)
pressure_box.place(x=770, y=435)


# ---------------- RUN APPLICATION ---------------- #

root.mainloop()
