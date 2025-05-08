# Step-by-Step Guide: Running the CoWIN Vaccine Slot Checker Script

This guide provides clear instructions on how to set up and execute the provided Python script to monitor CoWIN vaccine slot availability for a specific district.

## Prerequisites

Before you begin, ensure you have the following installed on your computer:

* **Python 3.x:** You need a working installation of Python 3. If you don't have it, download the installer from [python.org](https://www.python.org/downloads/). During installation on Windows, **it is highly recommended to check the option "Add Python to PATH"**.
* **The Python Script:** You need the actual Python code for the CoWIN Vaccine Slot Checker. Make sure you have saved the code in a file with a `.py` extension.

## Step 1: Install Required Libraries

The script uses the `requests` library to interact with the CoWIN API over the internet. You need to install this library.

1.  Open your terminal or command prompt.
    * On Windows, search for `Command Prompt` or `CMD`.
    * On macOS or Linux, search for `Terminal`.
2.  Execute the following command and press Enter:
    ```bash
    pip install requests
    ```
    This command uses `pip` (Python's package installer) to download and install the `requests` library.

## Step 2: Save the Python Code

If you haven't already, save the Python code for the slot checker:

1.  Copy the entire Python code.
2.  Open a plain text editor (such as VS Code, Sublime Text, Atom, Notepad++, or even the default Notepad on Windows or TextEdit on macOS).
3.  Paste the copied code into the editor.
4.  Save the file. Choose a descriptive name ending with `.py`, for example, `cowin_checker.py`. **Remember the location** where you save this file on your computer.

## Step 3: Configure the Script

Customize the script to check for slots according to your specific needs.

1.  Open the Python file (`cowin_checker.py` or whatever you named it) in your text editor.
2.  Locate the section starting with the comment `# CONFIGURATION`.
3.  Modify the values for the following variables:
    * `DISTRICT_ID`: Find the numerical ID for your desired district and replace `***` with it. You can often find these IDs by searching online or using tools that interact with the CoWIN API.
    * `CHECK_INTERVAL`: Change the value (default is `60`) to set how often the script checks for slots, in seconds. A value of `60` means it checks every minute.
    * `AGE_LIMIT`: Set this to `18` if you are looking for slots for ages 18 and above, or `45` for ages 45 and above.
    * `MIN_DOSES`: Set this to the minimum number of vaccine doses that must be available at a center for the script to consider it a valid slot and notify you (default is `1`).
4.  Save the file after making your configuration changes.

## Step 4: Run the Script

Now you can execute the script from your terminal or command prompt.

1.  Open your terminal or command prompt (if it's not already open from Step 1).
2.  Use the `cd` command to change the current directory to the folder where you saved your `cowin_checker.py` file.
    * Example (Windows): If your file is in `C:\Users\YourName\Documents\PythonScripts`, type `cd C:\Users\YourName\Documents\PythonScripts` and press Enter.
    * Example (macOS/Linux): If your file is in `/Users/YourName/Documents/PythonScripts`, type `cd /Users/YourName/Documents/PythonScripts` and press Enter.
3.  Once you are in the correct directory, run the script using the command:
    ```bash
    python cowin_checker.py
    ```
4.  Press Enter.

## Step 5: Monitor for Slots

* The script will print a starting message and then begin its checking loop.
* Every `CHECK_INTERVAL` seconds, it will fetch data from the CoWIN API.
* If no slots matching your criteria are found, it will print a "No slots available" message with a timestamp.
* If available slots are found, it will print an alert (`🚨 Slots available!`) followed by details for each matching center, including the name, pincode, date, vaccine type, and number of available doses.

## Step 6: Stop the Script

To stop the script from running, go back to the terminal or command prompt window where the script is active and press `Ctrl + C` on your keyboard.

This completes the process of setting up and running the CoWIN Vaccine Slot Checker script.
