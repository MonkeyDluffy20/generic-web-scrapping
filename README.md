# Recursive Web Scraper with Selenium and BeautifulSoup

This repository contains a Python script that recursively scrapes text from a website using Selenium for navigation and BeautifulSoup for parsing HTML content. The script extracts text from the URL and all linked pages within the same domain.

## Features

- Recursively scrape text from a website
- Handle relative and absolute URLs
- Avoid re-visiting already scraped URLs
- Easy to use with minimal setup

## Requirements

- Python 3.8 or higher
- Selenium
- BeautifulSoup4
- WebDriver for your browser (e.g., ChromeDriver for Google Chrome)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/recursive-web-scraper.git
    cd recursive-web-scraper
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install selenium beautifulsoup4
    ```

4. Download the appropriate WebDriver for your browser:
    - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for Google Chrome

5. Ensure the WebDriver executable is in your system's PATH or specify its path in the script.

## Usage

1. Open the terminal and navigate to the project directory.

2. Run the script:
    ```bash
    python scraper.py
    ```

3. When prompted, enter the URL of the website you want to scrape.

4. The script will navigate through the website, extracting and printing text from the initial page and all linked pages within the same domain.

## Example

```bash
Enter the URL of the website: https://example.com
Text 1:
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
...

Text 2:
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
...

...

Text N:
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.
