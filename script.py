import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

# The URL of the webpage containing the PDFs
url = "https://www.molinahealthcare.com/providers/il/medicaid/resource/Molina-Medical-Coverage-Guidelines.aspx"

# Directory where you want to save the PDFs
output_dir = "downloaded_pdfs"

# Create the directory if it doesn't exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Set custom headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send a GET request to the webpage
response = requests.get(url, headers=headers)

# Check if the request was successful
response.raise_for_status()

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.text, "html.parser")

# Find all links ending with .pdf
pdf_links = soup.find_all('a', href=True)

for link in pdf_links:
    href = link['href']
    if href.endswith('.pdf'):
        pdf_url = urljoin(url, href)
        pdf_name = os.path.join(output_dir, os.path.basename(href))

        # Retry logic for downloading the PDF
        retries = 3
        for attempt in range(retries):
            try:
                # Download the PDF
                with requests.get(pdf_url, headers=headers, stream=True) as r:
                    r.raise_for_status()  # Check if the request was successful
                    with open(pdf_name, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            f.write(chunk)
                print(f"Downloaded: {pdf_name}")
                break  # Exit retry loop on success
            except requests.exceptions.RequestException as e:
                print(f"Failed to download {pdf_url}: {e}")
                if attempt < retries - 1:
                    print("Retrying...")
                    time.sleep(2)  # Wait before retrying
                else:
                    print("Skipping to next file.")

print("Download process completed.")
