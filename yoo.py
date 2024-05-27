from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from urllib.parse import urlparse
import os

# Define extract_text_recursive function
def extract_text_recursive(url, base_url, visited_urls=set(), file_paths=[]):
    driver.get(url)
    time.sleep(2)

    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")
    text = soup.get_text(strip=True)

    # Create a unique file name for each webpage
    file_name = "text_" + str(len(visited_urls)) + ".txt"
    file_path = os.path.join(output_folder, file_name)
    file_paths.append(file_path)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

    # Find all anchor tags with href attribute
    anchor_tags = soup.find_all('a', href=True)
    for tag in anchor_tags:
        next_url = tag['href']
        if next_url.startswith(base_url) or next_url.startswith('/'):
            if next_url.startswith('/'):
                next_url = base_url + next_url
            if next_url not in visited_urls:
                visited_urls.add(next_url)
                extract_text_recursive(next_url, base_url, visited_urls, file_paths)

# Define scrape_website function
def scrape_website(url, base_url):
    file_paths = []
    extract_text_recursive(url, base_url, file_paths=file_paths)
    return file_paths

# Initialize WebDriver
driver = webdriver.Chrome()

# Example usage
url = input("Enter the URL of the website: ")

# Extract the base URL
parsed_url = urlparse(url)
base_url = parsed_url.scheme + '://' + parsed_url.netloc

# Create a folder to store all text files
output_folder = r"C:\Users\surya\OneDrive\Desktop\generic webscrapping\text_files"
os.makedirs(output_folder, exist_ok=True)

file_paths = scrape_website(url, base_url)

print("Text extracted from all visited websites has been saved to:", output_folder)

# Close WebDriver
driver.quit()
