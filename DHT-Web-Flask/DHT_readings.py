#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
import Adafruit_DHT
import time
import datetime # To get the current timestamp

# --- Flask App Setup ---
app = Flask(__name__)

# --- DHT11 Sensor Configuration ---
SENSOR_TYPE = Adafruit_DHT.DHT11
# GPIO pin where the DHT11 data line is connected (BCM numbering)
# This corresponds to physical pin 7 on the Raspberry Pi header
GPIO_PIN = 4

# --- Function to Read DHT11 Data ---
def read_dht_data():
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR_TYPE, GPIO_PIN)

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if humidity is not None and temperature is not None:
        # Round to one decimal place for display
        return {
            "temperature": round(temperature, 1),
            "humidity": round(humidity, 1),
            "timestamp": current_time,
            "error": None
        }
    else:
        return {
            "temperature": "N/A",
            "humidity": "N/A",
            "timestamp": current_time,
            "error": "Failed to retrieve data"
        }

# --- Flask Route ---
@app.route('/')
def index():
    sensor_data = read_dht_data()

    # Render the HTML template and pass the sensor data to it
    return render_template(
        'index.html',
        temperature=sensor_data["temperature"],
        humidity=sensor_data["humidity"],
        timestamp=sensor_data["timestamp"]
    )

# --- Run the Flask Application ---
if __name__ == '__main__':
    # To make the server accessible from other devices on your network,
    # set host='0.0.0.0'. For development, you can use debug=True for auto-reloading
    # and detailed error messages, but disable in production.
    app.run(host='0.0.0.0', port=5000, debug=False) # Set debug=True during development