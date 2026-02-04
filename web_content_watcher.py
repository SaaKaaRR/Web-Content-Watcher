import requests
import time
import sys
import argparse
from datetime import datetime
from bs4 import BeautifulSoup

def get_content(url, selector):
    """Generic fetcher using CSS Selectors."""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Use select_one for CSS selectors (like #id, .class, or div > b)
            target = soup.select_one(selector)
            if target:
                return target.get_text(strip=True)
    except Exception as e:
        return f"Error: {str(e)}"
    return None

def main():
    # 1. Setup Argument Parser
    parser = argparse.ArgumentParser(description="Universal Static Web Content Watcher")
    parser.add_argument("--url", required=True, help="The URL of the website to track")
    parser.add_argument("--selector", required=True, help="The CSS Selector for the content (e.g. '#price', '.rate-value')")
    parser.add_argument("--freq", type=int, default=30, help="Check frequency in seconds (default: 30)")
    
    args = parser.parse_args()

    print(f"🚀 Universal Watcher Started")
    print(f"Target URL: {args.url}")
    print(f"Selector:   {args.selector}")
    print(f"Frequency:  Every {args.freq}s")
    print("-" * 60)

    last_value = None

    try:
        while True:
            current_value = get_content(args.url, args.selector)

            if current_value:
                # If value changed or it's the first run
                if current_value != last_value:
                    now = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
                    label = " [INITIAL]" if last_value is None else " [CHANGED] 🔔"
                    print(f"\n[{now}] Value: {current_value}{label}")
                    last_value = current_value
                else:
                    # Heartbeat
                    ts = datetime.now().strftime('%H:%M:%S')
                    sys.stdout.write(f"\r[Last Check: {ts}] Content stable... ")
                    sys.stdout.flush()
            else:
                sys.stdout.write(f"\r[Error] Could not find content with that selector.   ")
                sys.stdout.flush()

            time.sleep(args.freq)

    except KeyboardInterrupt:
        print("\n\n👋 Watcher stopped. Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    main()