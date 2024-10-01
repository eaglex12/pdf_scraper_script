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


