import requests
import os
from dotenv import load_dotenv

load_dotenv()

def extract_from_scopus(query, year_start, year_end):
    api_key = os.getenv("SCOPUS_API_KEY")
    if not api_key:
        print("Error: Scopus API key not found")
        return None

    base_url = "https://api.elsevier.com/content/search/scopus"
    
    headers = {
        "Accept": "application/json",
        "X-ELS-APIKey": api_key
    }
    
    params = {
        "query": f'TITLE-ABS-KEY({query}) AND PUBYEAR > {year_start} AND PUBYEAR < {year_end}',
        "count": 25,
    }
    
    try:
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to the Scopus API: {e}")
        return None

if __name__ == '__main__':
    data = extract_from_scopus("machine learning", 2020, 2023)
    if data:
        print("Data successfully extracted")
    else:
        print("The extraction failed")
