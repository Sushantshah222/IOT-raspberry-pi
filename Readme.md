# IOT-RASPBERRY-PI: Basics of Sensor Reading and Web Control

This repository contains basic Internet of Things (IoT) projects demonstrating how to interact with physical components (like DHT11 sensor and LED) using a Raspberry Pi, controlled via Python scripts and Flask web servers.

## Table of Contents
1.  [Project Structure](#1-project-structure)
2.  [Prerequisites](#2-prerequisites)
    * [Hardware](#hardware)
    * [Software](#software)
3.  [Setup Instructions](#3-setup-instructions)
    * [Clone the Repository](#clone-the-repository)
    * [Create and Activate Virtual Environment](#create-and-activate-virtual-environment)
    * [Install Python Dependencies](#install-python-dependencies)
    * [Install System-Level GPIO Dependencies](#install-system-level-gpio-dependencies)
4.  [Hardware Connections](#4-hardware-connections)
    * [DHT11 Temperature & Humidity Sensor](#dht11-temperature--humidity-sensor)
    * [LED Control](#led-control)
5.  [Running the Applications](#5-running-the-applications)
    * [Normal DHT Readings (Console)](#normal-dht-readings-console)
    * [DHT Web Flask Server](#dht-web-flask-server)
    * [LED Web Control Server](#led-web-control-server)
6.  [Troubleshooting Common Issues](#6-troubleshooting-common-issues)
7.  [Next Steps / Future Enhancements](#7-next-steps--future-enhancements)

---

### 1. Project Structure

This repository is organized into distinct directories for different functionalities:

I will provide all the information in a single README.md file, as requested.

Markdown

# IOT-RASPBERRY-PI: Basics of Sensor Reading and Web Control

This repository contains basic Internet of Things (IoT) projects demonstrating how to interact with physical components (like DHT11 sensor and LED) using a Raspberry Pi, controlled via Python scripts and Flask web servers.

## Table of Contents
1.  [Project Structure](#1-project-structure)
2.  [Prerequisites](#2-prerequisites)
    * [Hardware](#hardware)
    * [Software](#software)
3.  [Setup Instructions](#3-setup-instructions)
    * [Clone the Repository](#clone-the-repository)
    * [Create and Activate Virtual Environment](#create-and-activate-virtual-environment)
    * [Install Python Dependencies](#install-python-dependencies)
    * [Install System-Level GPIO Dependencies](#install-system-level-gpio-dependencies)
4.  [Hardware Connections](#4-hardware-connections)
    * [DHT11 Temperature & Humidity Sensor](#dht11-temperature--humidity-sensor)
    * [LED Control](#led-control)
5.  [Running the Applications](#5-running-the-applications)
    * [Normal DHT Readings (Console)](#normal-dht-readings-console)
    * [DHT Web Flask Server](#dht-web-flask-server)
    * [LED Web Control Server](#led-web-control-server)
6.  [Troubleshooting Common Issues](#6-troubleshooting-common-issues)
7.  [Next Steps / Future Enhancements](#7-next-steps--future-enhancements)

---

### 1. Project Structure

This repository is organized into distinct directories for different functionalities:

IOT-RASPBERRY-PI/
├── DHT-Web-Flask/             # Flask web server to display DHT11 data on a webpage
│   ├── templates/             # HTML templates for the Flask app
│   └── DHT_readings.py        # Main Flask application for DHT web display
├── normal_dht_reading/        # Python script for basic DHT11 readings to console
│   └── normal_dht_read.py     # Script to read DHT11 and print to terminal
├── ON-OFF_led/                # Flask web server to control a physical LED
│   ├── templates/             # HTML templates for the LED control web interface
│   └── led_app.py             # Main Flask application for LED control
└── requirements.txt           # List of all Python dependencies for the project



---

### 2. Prerequisites

#### Hardware
* **Raspberry Pi:** Any model (e.g., Raspberry Pi Zero 2 W).
* **MicroSD Card:** With Raspberry Pi OS (preferably Lite or Desktop version) installed.
* **DHT11 Sensor:** Temperature and Humidity Sensor.
* **LED:** Any standard LED.
* **Resistor:** 220-330 Ohm resistor (for the LED).
* **Jumper Wires:** Male-to-male and male-to-female.
* **Breadboard:** (Recommended) for easy prototyping.

#### Software
* **Python 3:** Pre-installed on Raspberry Pi OS.
* **`pip`:** Python package installer (usually `pip3` on Pi).
* **`git`:** For cloning the repository.
* **Terminal access:** Via SSH or directly connected monitor/keyboard.

---

### 3. Setup Instructions

Follow these steps to set up the project environment on your Raspberry Pi.

#### Clone the Repository

First, clone this repository to your Raspberry Pi:

```bash
cd ~ # Go to your home directory
git clone [https://github.com/YOUR_USERNAME/IOT-RASPBERRY-PI.git](https://github.com/YOUR_USERNAME/IOT-RASPBERRY-PI.git) # Replace YOUR_USERNAME with your GitHub username
cd IOT-RASPBERRY-PI



## Setup Instructions

Follow these steps to set up the project environment on your Raspberry Pi.

#### Create and Activate Virtual Environment

It's highly recommended to use a Python virtual environment to manage project dependencies and avoid conflicts with system-wide packages.

1.  **Navigate to your project directory:**
    ```bash
    cd ~/IOT-RASPBERRY-PI # Or the specific directory where you want to create the venv
    ```
2.  **Create the virtual environment:**
    ```bash
    python3 -m venv venv
    ```
    This command creates a new directory named `venv` (you can choose a different name) inside your current directory, containing a copy of the Python interpreter and `pip`.

3.  **Activate the virtual environment:**
    ```bash
    source venv/bin/activate
    ```
    You will see `(venv)` at the beginning of your terminal prompt, indicating the virtual environment is active. All subsequent `pip` commands will install packages into this isolated environment.

#### Install Python Dependencies

Once your virtual environment is active, install all required Python libraries listed in `requirements.txt`:

```bash
pip install -r requirements.txt