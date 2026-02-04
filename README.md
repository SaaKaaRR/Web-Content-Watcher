# 🌐 Universal Web Watcher

A lightweight, dynamic Python engine designed to monitor specific content on any static website.  
Whether you're tracking gold prices, stock values, or news headlines, this script alerts you the moment a change is detected.

---

## 🚀 Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/universal-web-watcher.git
cd universal-web-watcher
pip install -r requirements.txt
🛠️ Usage
Run the script by passing the --url, --selector, and --freq (frequency in seconds) arguments.

⚠️ Important: Quotation Marks
When using CSS selectors with special characters like #, >, or :, you must wrap the selector in double quotes to prevent terminal errors.

📌 Examples
Monitor Nepal Gold Prices (Fine Gold)
python3 universal_watcher.py \
  --url "https://www.fenegosida.org/" \
  --selector "#header-rate:nth-of-type(2) b:nth-of-type(1)" \
  --freq 10
Monitor a News Headline
python3 universal_watcher.py \
  --url "https://kathmandupost.com/" \
  --selector "h1.title" \
  --freq 300
🔍 How to Find a CSS Selector
Open the target website in Chrome

Right-click the element you want to track and select Inspect

In the Elements panel, right-click the highlighted code

Select Copy → Copy Selector

Paste that selector into the --selector argument of this script

📋 Requirements
The project relies on the following libraries:

requests — For fetching web content

beautifulsoup4 — For parsing HTML and locating data via selectors

🗺️ Roadmap
 📱 Phone Notifications: Integrate Telegram and Pushbullet alerts

 ⚙️ Dynamic Site Support: Support for JavaScript-heavy sites using Selenium / Playwright

 📊 CSV Logging: Automatically save price history to a local database

⚖️ License
This project is licensed under the MIT License.
