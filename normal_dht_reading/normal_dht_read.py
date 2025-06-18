# !/usr/bin/env python

import Adafruit_DHT # This library handles the complex timing using RPi.GPIO internally
import time

# --- Sensor & GPIO Pin Configuration ---
# Sensor type: Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302
SENSOR_TYPE = Adafruit_DHT.DHT11

# GPIO pin where the DHT11 data line is connected (BCM numbering)
# This corresponds to physical pin 7 on the Raspberry Pi header
GPIO_PIN = 4

print("Starting DHT11 sensor readings (using Adafruit_DHT library)...")
print("Press Ctrl+C to stop.")
print("-" * 30)

try:
    while True:
        # Attempt to get sensor reading. read_retry will retry up to 15 times
        # waiting 2 seconds between each retry, which is good for reliability.
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR_TYPE, GPIO_PIN)

        # Check if valid data was received
        if humidity is not None and temperature is not None:
            # Display the readings
            print(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Temperature: {temperature:.1f}°C")
            print(f"Humidity:    {humidity:.1f}%")
            print("-" * 30)

        else:
            # If readings are None, it means the sensor couldn't be read.
            print("Failed to retrieve data from sensor. Retrying...")
            print("-" * 30)

        time.sleep(2) # Wait 2 seconds before the next reading attempt

except KeyboardInterrupt:
    # Handle Ctrl+C to exit cleanly
    print("\nProgram stopped by user.")

except Exception as e:
    # Catch any other unexpected errors
    print(f"An unexpected error occurred: {e}")

# Note: Adafruit_DHT handles GPIO cleanup internally for its operations,
# so an explicit GPIO.cleanup() is often not strictly necessary here,
# unless you were doing other direct RPi.GPIO operations in the same script.
# For simplicity and robust practice, if you use RPi.GPIO directly anywhere else,
# ensure cleanup.