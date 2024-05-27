from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from urllib.parse import urlparse

# Define extract_text_recursive function
def extract_text_recursive(url, base_url, visited_urls=set(), extracted_texts=[]):
    driver.get(url)
    time.sleep(2)

    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")
    text = soup.get_text(strip=True)

    extracted_texts.append(text)  # Append extracted text to the list

    # Find all anchor tags with href attribute
    anchor_tags = soup.find_all('a', href=True)
    for tag in anchor_tags:
        next_url = tag['href']
        if next_url.startswith(base_url) or next_url.startswith('/'):
            if next_url.startswith('/'):
                next_url = base_url + next_url
            if next_url not in visited_urls:
                visited_urls.add(next_url)
                extract_text_recursive(next_url, base_url, visited_urls, extracted_texts)

# Define scrape_website function
def scrape_website(url, base_url):
    extracted_texts = []
    extract_text_recursive(url, base_url, extracted_texts=extracted_texts)
    return extracted_texts

# Initialize WebDriver
driver = webdriver.Chrome()

# Example usage
url = input("Enter the URL of the website: ")

# Extract the base URL
parsed_url = urlparse(url)
base_url = parsed_url.scheme + '://' + parsed_url.netloc

extracted_texts = scrape_website(url, base_url)

# Print extracted texts
for i, text in enumerate(extracted_texts):
    print(f"Text {i+1}:")
    print(text)
    print()

# Close WebDriver
driver.quit()
