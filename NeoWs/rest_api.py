import requests
from NeoWs.neo_utils import get_dates_by_user_for_neo

key = "DEMO_KEY"


def get_neo_data_by_dates():
    start_date, end_date = get_dates_by_user_for_neo()
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={key}"
    response = requests.get(url).json()
    return response
