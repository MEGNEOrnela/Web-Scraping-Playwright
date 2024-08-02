# 🔍 Playwright-based web scraping

This repository consists of a basic method to communicate with a web browser (Chromium) and scrape dynamic web content using the [Playwright](https://playwright.dev/) tool. 

The `main.py` file contains the code to navigate to a URL and scroll over it. We will collect dynamic items like title, url, and author while parsing the output into a dictionary.

Below are the instructions to run the script:

1. Install the requirements
```bash
python3 -m venv env
source env/bin/activate 
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
```
2. Install Playwright browsers
```bash
playwright install
```

3. Run the `main.py` file
```bash
python3  main.py
```
