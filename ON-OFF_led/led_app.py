#!/usr/bin/env python


from flask import Flask, render_template, redirect, url_for
import RPi.GPIO as GPIO # Import the RPi.GPIO library
import time # For optional delays

# --- Flask App Setup ---
app = Flask(__name__)

# --- GPIO Setup for LED ---
LED_PIN = 17 # Using BCM numbering for GPIO 17 (physical pin 11)

GPIO.setmode(GPIO.BCM) # Use BCM numbering
GPIO.setwarnings(False) # Disable warnings for cleaner output
GPIO.setup(LED_PIN, GPIO.OUT) # Set the LED pin as an output

# Initial LED state (optional, can be ON/OFF when script starts)
current_led_state = GPIO.LOW # Start with LED OFF (GPIO.LOW means 0V)
GPIO.output(LED_PIN, current_led_state) # Ensure LED is off at start

# --- Flask Routes ---

@app.route('/')
def index():
    # Determine current status text for display
    status_text = "ON" if GPIO.input(LED_PIN) == GPIO.HIGH else "OFF"
    return render_template('led_control.html', status=status_text)

@app.route('/led/<action>')
def control_led(action):
    global current_led_state # Declare global to modify the variable outside this function

    if action == 'on':
        GPIO.output(LED_PIN, GPIO.HIGH) # Turn LED ON (3.3V)
        current_led_state = GPIO.HIGH
        print("LED turned ON")
    elif action == 'off':
        GPIO.output(LED_PIN, GPIO.LOW) # Turn LED OFF (0V)
        current_led_state = GPIO.LOW
        print("LED turned OFF")
    else:
        print(f"Invalid action: {action}")

    # Redirect back to the main page to show the updated status
    return redirect(url_for('index'))

# --- Run the Flask Application ---
if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=False) # Run on all interfaces, port 5000

    except KeyboardInterrupt:
        # Clean up GPIO settings on program exit (Ctrl+C)
        print("\nShutting down server and cleaning up GPIO...")
    finally:
        GPIO.cleanup() # This is crucial to release GPIO pins
        print("GPIO cleanup complete. Server stopped.")
