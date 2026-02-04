# 🌐 Universal Web Watcher

A lightweight, high-performance Python engine designed to monitor specific content on any static website. Whether you're tracking gold prices, stock values, or news headlines, this script alerts you the moment a change is detected.



## ✨ Features
* **Universal Tracking**: Works with any website by providing a simple CSS selector.
* **Smart Monitoring**: Only alerts you when the value actually changes, preventing terminal clutter.
* **Live Heartbeat**: Real-time status updates showing the last successful check time on a single line.
* **Custom Frequency**: Full control over how often the script checks the target site to avoid IP blocks.
* **Graceful Exit**: Cleanly handles `Ctrl+C` shutdowns without showing messy error traces.

## 🚀 Getting Started

### 1. Prerequisites
* **Python 3.6+**: Ensure you have Python installed.
* **Terminal**: Access to a command prompt, PowerShell, or terminal window.

### 2. Installation
Clone this repository and install the required dependencies:

```bash
git clone [https://github.com/yourusername/universal-web-watcher.git](https://github.com/yourusername/universal-web-watcher.git)
cd universal-web-watcher
pip install -r requirements.txt
🛠️ Usage
Run the script by passing the --url, --selector, and --freq arguments.

⚠️ Important: When using CSS selectors with special characters like #, >, or :, you must wrap the selector in double quotes to prevent the terminal from misinterpreting the symbols.

Examples
Monitor Gold Prices (Fine Gold)

Bash
python3 universal_watcher.py --url "[https://www.fenegosida.org/](https://www.fenegosida.org/)" --selector "#header-rate:nth-of-type(2) b:nth-of-type(1)" --freq 10
Monitor a News Headline

Bash
python3 universal_watcher.py --url "[https://kathmandupost.com/](https://kathmandupost.com/)" --selector "h1.title" --freq 300
🔍 How to Find a CSS Selector
If you aren't sure what selector to use for a specific value:

Open the target website in Chrome.

Right-click the exact value or price you want to track and select Inspect.

In the Elements panel that opens, right-click the highlighted HTML code.

Select Copy > Copy Selector.

Paste that string into the --selector argument (always wrap it in quotes).

📋 Requirements
The project relies on the following libraries:

requests: For fetching web content.

beautifulsoup4: For parsing HTML and locating data via selectors.

🗺️ Roadmap
[ ] Mobile Notifications: Integrate Telegram and Pushbullet alerts.

[ ] Dynamic Site Support: Add Selenium support for JavaScript-heavy sites.

[ ] Data Logging: Save price history to a local CSV or SQLite database.

[ ] Multi-Watcher: Monitor multiple URLs simultaneously from a single config file.

⚖️ License
This project is licensed under the MIT License - see the LICENSE file for details.
