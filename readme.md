# Binance Listing Bot

## Overview

The Binance Listing Bot is a Python script designed to monitor new listings on Binance and notify users through various channels such as email, Discord, and phone calls. The script regularly checks for new announcements and alerts users when a new cryptocurrency is listed on Binance and buy on Gate.io.

## Features

- **Email Notification:** Receive email alerts for new listings.
- **Discord Notification:** Get notifications on Discord through a webhook.
- **Phone Call Alert:** Receive a phone call notification using Twilio.

## Setup

1. **Install Dependencies:**
    - Make sure you have Python installed.
    - Install required Python packages using `pip install -r requirements.txt`.

2. **Configuration:**
    - Open the script and update the following configuration variables:
        - Email credentials: `sender_address`, `sender_pass`, `receiver_addresses`
        - Discord webhook URL: `discord_webhook_url`, `discord_headers`
        - Twilio credentials: `twilio_account_sid`, `twilio_auth_token`, `twilio_from_number`, `twilio_to_number`

3. **Run the Script:**
    - Execute the script using `python main.py`.

## Usage

The script will run indefinitely, periodically checking for new listings on Binance. Notifications will be sent based on the configured channels.

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback and improvements are welcome!

## License

This project is licensed under the [MIT License](LICENSE).

---

**Note:** Replace placeholder values in the script with your actual credentials and configuration details.
