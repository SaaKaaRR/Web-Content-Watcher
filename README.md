Markdown
# 🌐 Universal Web Watcher

A lightweight, dynamic Python engine designed to monitor specific content on any static website. Whether you're tracking gold prices, stock values, or news headlines, this script alerts you the moment a change is detected.



## ✨ Features
* **Universal Tracking**: Works with any website by providing a simple CSS selector.
* **Smart Monitoring**: Only alerts you when the value actually changes, preventing terminal clutter.
* **Live Heartbeat**: Real-time status updates showing the last successful check time.
* **Custom Frequency**: Control how often the script checks the target site to avoid IP blocks.
* **Clean Exit**: Gracefully handles `Ctrl+C` for a smooth shutdown.

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.6 or higher
* A terminal/command prompt.

### 2. Installation
Clone this repository and install the required dependencies:

```bash
git clone [https://github.com/yourusername/universal-web-watcher.git](https://github.com/yourusername/universal-web-watcher.git)
cd universal-web-watcher
pip install -r requirements.txt
🛠️ Usage
Run the script by passing the --url, --selector, and --freq (frequency in seconds) arguments.

⚠️ Important: Quotation Marks
When using CSS selectors with special characters like #, >, or :, you must wrap the selector in double quotes to prevent terminal errors.

Examples
Monitor Nepal Gold Prices (Fine Gold)

Bash
python3 universal_watcher.py --url "[https://www.fenegosida.org/](https://www.fenegosida.org/)" --selector "#header-rate:nth-of-type(2) b:nth-of-type(1)" --freq 10
Monitor a News Headline

Bash
python3 universal_watcher.py --url "[https://kathmandupost.com/](https://kathmandupost.com/)" --selector "h1.title" --freq 300
🔍 How to Find a CSS Selector
Open the target website in Chrome.

Right-click the element you want to track and select Inspect.

In the Elements panel, right-click the highlighted code.

Select Copy > Copy Selector.

Paste that selector into the --selector argument of this script.

📋 Requirements
The project relies on the following libraries:

requests: For fetching web content.

beautifulsoup4: For parsing HTML and locating data via selectors.

🗺️ Roadmap
[ ] Phone Notifications: Integrate Telegram and Pushbullet alerts.

[ ] Dynamic Site Support: Support for JavaScript-heavy sites using Selenium/Playwright.

[ ] CSV Logging: Automatically save price history to a local database.

⚖️ License
This project is licensed under the MIT License.


***

### 💡 Quick Tip for GitHub Upload:
When you create a new repository on GitHub, it will ask if you want to add a README. You can choose "Yes," or simply upload this file. GitHub will automatically detect the `.md` extension and render it with the beautiful formatting (bolding, code blocks, and icons) you see above.