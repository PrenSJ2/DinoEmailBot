# Dino Email Bot

Dino Email Bot is a Python script that automates the process of finding emails in Gmail containing the word "sentry", opening them, and checking for a "View on Sentry" button. If the button is present, the script navigates to the Sentry page, checks for a specific link, and then either deletes or marks the email as unread based on the presence of the link.

## Prerequisites

- Python 3.6 or higher
- Selenium WebDriver
- Google Chrome browser

## Installation

1. Clone the repository or download the source files.

2. Set up a virtual environment (optional, but recommended):
```
python -m venv env
source env/bin/activate # For Unix-based systems
env\Scripts\activate # For Windows
```

3. Install the required dependencies:

`pip install -r requirements.txt`


## Starting Chrome in Debugging Mode

Before running the Dino Email Bot script, you need to start your Chrome browser in debugging mode. This allows the script to connect to an existing Chrome instance that is already logged into Gmail.

1. Close all running instances of Google Chrome.

2. Open a terminal (command prompt or PowerShell on Windows) and run the following command:

For Unix-based systems (macOS and Linux)

`'/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome' --remote-debugging-port=9222`

For Windows

`"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222`



3. Log in to your Gmail account in the Chrome instance that opens.

4. Log in to your Sentry account in the Chrome instance that opens.

## Running the Script

With Chrome running in debugging mode and logged into Gmail, run the Dino Email Bot script:

`python main.py`

The script will connect to the existing Chrome instance, search for emails containing the word "sentry", and perform the specified actions based on the presence of a link in the Sentry page.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
