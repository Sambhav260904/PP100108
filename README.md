# PP100108 Repository

Welcome to the PP100108 repository! This repository contains three projects demonstrating various Python skills—from command-line tools to data analysis and web scraping.

## Projects Overview

### 1. Command-Line Calculator
**Objective:**  
Create a command-line calculator that performs basic arithmetic operations.

**Key Features:**
- Performs addition, subtraction, multiplication, and division.
- Handles division by zero with appropriate error messages.
- Provides user-friendly prompts for input.
- Optionally includes advanced operations such as square root and exponentiation.

**Usage:**  
Run the `calculator.py` script from the command line to perform calculations. Follow the on-screen instructions to input numbers and select the operation.

---

### 2. Basic Data Analysis
**Objective:**  
Write a script to analyze a CSV file and display statistical measures.

**Key Features:**
- Calculates and displays the average, maximum, and minimum values of a specified numerical column.
- Allows users to specify the column to analyze.
- Handles missing or invalid data gracefully.
- Optionally visualizes data using Matplotlib.

**Usage:**  
Run the `data_analysis.py` script, provide the CSV file name and the column you wish to analyze, and review the output statistics and optional visualizations.

---

### 3. Web Scraper
**Objective:**  
Develop a script to scrape data from a website.

**Key Features:**
- Fetches data (e.g., quotes, headlines, product details) from a public website.
- Saves the scraped data into a CSV or JSON file.
- Implements basic error handling for network issues.
- Optionally supports pagination to scrape multiple pages of data.

**Usage:**  
Run the `web_scraper.py` script to extract and save the desired data. The script automatically detects the end of available pages and handles any network errors gracefully.

---

## Setup and Installation

Before running the scripts, ensure that you have Python 3 installed along with the necessary libraries. You can install required libraries using `pip`. For example:

```bash
pip install requests beautifulsoup4 matplotlib pandas
