import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('EIA_API_KEY')

def fetch_eia_energy_data(start_year, end_year, length=5000):
    """
    Function to get energy data from the EIA API.
    
    url: https://www.eia.gov/opendata/browser/
    """
    base_url = "https://api.eia.gov/v2/electricity/electric-power-operational-data/data/"
    headers = { "X-Params": {
            "frequency": "annual",
            "data": [
                "cost-per-btu",
                "generation",
                "receipts",
                "total-consumption"
            ],
            "facets": {},
            "start": str(start_year),
            "end": str(end_year),
            "sort": [
                {
                    "column": "period",
                    "direction": "desc"
                }
            ],
            "offset": 0,
            "length": length
        }
    }

    params = {
        "api_key": API_KEY
    }

    #call the API
    response = requests.get(base_url, headers={"accept": "application/json"}, params=params)

    if response.status_code != 200:
        raise Exception(f"Error fetching data: {response.status_code} - {response.text}")
    
    data = response.json()

    return data

if __name__ == "__main__":
    start_year = 2010
    end_year = 2020
    try:
        energy_data = fetch_eia_energy_data(start_year, end_year)
        print(energy_data)
    except Exception as e:
        print(f"An error occurred: {e}")