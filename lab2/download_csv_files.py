import os
import requests

# List of CSV URLs
csv_urls = [
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Final%20Assignment/DimDate.csv",
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Final%20Assignment/DimTruck.csv",
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Final%20Assignment/DimStation.csv",
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Final%20Assignment/FactTrips.csv"
]

# Target folder
output_dir = os.path.join("tmp", "csv")
os.makedirs(output_dir, exist_ok=True)

for url in csv_urls:
    try:
        filename = url.split("/")[-1]
        filepath = os.path.join(output_dir, filename)

        print(f"Downloading {filename}...")
        response = requests.get(url)
        response.raise_for_status()  # Raise error on bad status

        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"Saved to {filepath}")

    except Exception as e:
        print(f"Failed to download {url}: {e}")
