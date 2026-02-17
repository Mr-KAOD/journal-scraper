# Journal Extractor 🔍

An automated tool designed to find and extract official website URLs (Home) for scientific journals listed on Scimago. It features built-in stealth mechanisms to bypass bot detection.

---

## 🏗️ Project Status & Context
> **Note:** This is a **work in progress**.  
> This project is being developed as part of the research activities within a **Research Group (Semillero de Investigación)** at my university. It is currently in active development to support academic data collection.

---

## 🛠️ Setup & Installation

Follow these steps to set up the environment and install all necessary components on your local machine.

### 1. Clone the Repository
Open your terminal and run the following command:

    git clone git@github.com:mr-kaod/journal-scraper.git
    cd journal-scraper

### 2. Create and Activate a Virtual Environment
This ensures that the project dependencies are isolated from your global Python installation.
#### On Linux / macOS:

    python3 -m venv env
    source env/bin/activate

#### On Windows (PowerShell):

    python -m venv env
    .\env\Scripts\Activate.ps1

### 3. Install Python Dependencies
Once the environment is activated (indicated by (env) in your terminal prompt), install the required libraries:

    pip install -r requirements.txt

### 4. Install Playwright Browsers

Playwright requires specific browser binaries to operate. Install the Chromium engine by running:

    playwright install chromium

## 📈 Usage Guide

To run the extractor, follow these simple steps:

Start the script:

    python src/main.py

**Search:** When prompted in the terminal, enter a related keyword.

**Human Verification:** The browser will open in "headed" mode. If a Cloudflare or Captcha challenge appears, solve it manually in the browser window.

**Data Extraction:** Once verified, the script will automatically scrape the data and save a CSV file in the data/raw/ directory.

## 📁 Project Structure

src/: Contains the core Python scraping logic.

data/raw/: Destination for generated CSV reports (this folder is kept in the repo via .gitkeep).

requirements.txt: Minimal list of required Python packages for clean deployment.