import requests
from bs4 import BeautifulSoup
import pdfkit

# Base URL
base_url = "https://services3.horizon-bcbsnj.com/ddn/NJhealthWeb.nsf"

# Fetch the main page
response = requests.get(base_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all links to documents
    links = soup.find_all('a', href=True)
    
    # Filter links to get only those pointing to documents
    document_links = [
        link['href'] for link in links if link['href'].startswith('AllIndexDocuments/')
    ]
    
    # Process each document link
    for doc_link in document_links:
        # Construct the full URL
        full_url = f"{base_url}/{doc_link}?OpenDocument"
        
        # Fetch the document content
        doc_response = requests.get(full_url)
        
        if doc_response.status_code == 200:
            # HTML content to save as PDF
            html_content = doc_response.text
            
            # Extract the document name for saving
            doc_name = doc_link.split('/')[-1].replace('?OpenDocument', '') + '.pdf'
            
            # Save the HTML content as a PDF
            pdfkit.from_string(html_content, doc_name)
            print(f"PDF saved as '{doc_name}'")
        else:
            print(f"Failed to retrieve document from {full_url}. Status code: {doc_response.status_code}")
else:
    print(f"Failed to retrieve the main page. Status code: {response.status_code}")
