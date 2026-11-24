import requests
import json

start_date = "2026-10-01"
end_date = "2026-10-15"

server_url = "https://bucegiparkconnect.smartconservationtools.org/server"
query_uuid = "85a120e5-5499-4074-a6bc-eb9f19ee9f04"
api_url = f"{server_url}/api/query/custom/waypoint"

compiled_url = f"{server_url}{api_url}"

params = {
    "start_date": start_date,
    "end_date": end_date
}
headers = {
    "Authorization": "Bearer 7798f9b5-dafd-4c8f-85d0-d6a49f90f010"
}
username = 'bucegipark_admin'
password = '@BucegiP@rk24'

response = requests.get(compiled_url, auth=(username, password), params=params)

if response.status_code != 200:
    print(f"Eroare HTTP: {response.status_code}")
    print(response.json())
else:
    data = response.json()
    print(json.dumps(data, indent=2)[:2000])