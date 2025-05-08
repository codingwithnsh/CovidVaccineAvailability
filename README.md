# CoWIN Vaccine Slot Checker (Python Script)

A simple Python script to monitor available vaccine appointment slots for a specific district using the CoWIN public API.

## Overview

This script helps users find available vaccine slots that meet their criteria (age and minimum doses) without manually checking the CoWIN website repeatedly. It runs in the background and prints notifications to the console when slots are found.

## Features

* Fetches real-time data from the CoWIN API.
* Filters slots based on minimum age and available dose capacity.
* Checks for slots at a configurable interval.
* Prints available slots details to the console.

## Requirements

* Python 3.x
* The `requests` Python library

## Installation

1.  Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).
2.  Install the `requests` library using pip:
    ```bash
    pip install requests
    ```

## Configuration

Open the `vaccine_checker.py` file (or whatever you name the script) in a text editor. Modify the following variables in the `# CONFIGURATION` section:

* `DISTRICT_ID`: Replace `194` with the numerical ID of your desired district. You can find district IDs from various online sources or by exploring the CoWIN API documentation if you are technically inclined.
* `CHECK_INTERVAL`: The time in seconds between checks (default is 60 seconds).
* `AGE_LIMIT`: Set to `18` or `45` based on the age group you are looking for.
* `MIN_DOSES`: The minimum number of available doses required at a center to trigger an alert (default is 1).

## How to Run

1.  Save the code as a Python file (e.g., `vaccine_checker.py`).
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script using the command:
    ```bash
    python vaccine_checker.py
    ```
5.  The script will start checking for slots and print updates to the console. It will notify you with "🚨 Slots available!" when it finds centers matching your criteria.

## Notes

* The script checks for slots for the **current date** only.
* The script will run continuously until you stop it by pressing `Ctrl+C` in the terminal.
* Be mindful of the `CHECK_INTERVAL`. Checking too frequently might put unnecessary load on the CoWIN API.
* This script is a basic tool. For more advanced features (like notifications via email/SMS, checking multiple dates/districts), you would need to enhance the code.
* Ensure you comply with the CoWIN API usage policy.

## Disclaimer

This script is provided for informational purposes only. The availability of vaccine slots is subject to real-time updates on the CoWIN platform.

## Credits

* Uses the CoWIN public API.
* Developed in Python.
