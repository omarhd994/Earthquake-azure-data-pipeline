# Define ADLS Gen2 paths for data lake tiers
tiers = ["bronze", "silver", "gold"]
adls_paths = {tier: f"abfss://{tier}@dataomar123.dfs.core.windows.net/" for tier in tiers}

bronze_adls = adls_paths["bronze"]
silver_adls = adls_paths["silver"]
gold_adls = adls_paths["gold"]

# Check connectivity to each tier (optional but useful during dev/debug)
dbutils.fs.ls(bronze_adls)
dbutils.fs.ls(silver_adls)
dbutils.fs.ls(gold_adls)

import requests
import json
from datetime import date, timedelta

# Fetch data for the previous day
start_date = date.today() - timedelta(1)
end_date = date.today()

start_date, end_date

# Request USGS earthquake data in GeoJSON format
url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start_date}&endtime={end_date}"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json().get('features', [])

    if not data:
        print("No data returned for the specified date range.")
    else:
        # Persist raw data to bronze layer
        file_path = f"{bronze_adls}/{start_date}_earthquake_data.json"
        json_data = json.dumps(data, indent=4)
        dbutils.fs.put(file_path, json_data, overwrite=True)
        print(f"Data successfully saved to {file_path}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")

# Inspect first record (optional)
data[0]
