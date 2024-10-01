# PDF Scraper

A collection of scripts designed to automate the process of downloading PDF files from a specified webpage, utilizing various techniques for web scraping and automation.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [PDF Download Script](#pdf-download-script)
  - [Auto Clicker Script](#auto-clicker-script)
- [License](#license)

## Installation

To use the scripts in this repository, ensure you have Python 3.x installed on your machine. You'll also need to install the required libraries. You can do this using pip:

```bash
pip install requests beautifulsoup4 pyautogui
```

## Usage

### PDF Download Script

This script downloads all PDF files from a specified webpage.

- **File:** `script.py`
- **Requirements:** `requests`, `beautifulsoup4`
- **How to Use:**
  1. Open the script and modify the `url` variable to point to the desired webpage containing the PDFs.
  2. Optionally, change the `output_dir` variable to specify where you want to save the downloaded PDFs.
  3. Run the script:

```bash
python script.py
```

### Auto Clicker Script

This script automates mouse clicks at the current mouse position every second.

- **File:** `mouse.py`
- **Requirements:** `pyautogui`
- **How to Use:**
  1. Run the script to start the auto-clicking process. It will continue until interrupted.
  2. Press `Ctrl + C` in the terminal to stop the script.

```bash
python mouse.py
```

### Using JavaScript in Browser Console

If you don't want to use the Python script, you can run a JavaScript snippet directly in your browser's console to download PDF files from a webpage.

#### Instructions:

1. **Open the Webpage**: Go to the webpage that contains the PDF links you want to download.
2. **Open the Console**:
   - **Google Chrome**: Right-click on the page, select "Inspect," and then click on the "Console" tab.
   - **Mozilla Firefox**: Right-click on the page, select "Inspect Element," and then click on the "Console" tab.
   - **Microsoft Edge**: Right-click on the page, select "Inspect," and then click on the "Console" tab.
3. **Copy and Paste the Script**: Use the following JavaScript code snippet given in console.txt, which selects all `<a>` tags with hrefs ending in `.pdf` and automatically downloads them.
4. **Run the Script**: Press `Enter` after pasting the script into the console. The script will start downloading all the PDFs it finds on the page.

#### Notes:
- Ensure that pop-up blockers are disabled for the page, as some browsers may block automatic downloads.


