
import csv
import requests
from pathlib import Path

URL = (
    "https://api.worldbank.org/v2/country/VNM/"
    "indicator/SP.POP.TOTL"
)

OUTPUT_FILE = Path(__file__).with_name(
    "population_vietnam.csv"
)


def collect_population():
    params = {
        "format": "json",
        "date": "2000:2024",
        "per_page": 100
    }

    response = requests.get(URL, params=params, timeout=30)
    response.raise_for_status()

    result = response.json()
    records = result[1]

    data = []

    for record in records:
        if record["value"] is not None:
            data.append({
                "country": record["country"]["value"],
                "year": int(record["date"]),
                "population": int(record["value"])
            })

    return sorted(data, key=lambda row: row["year"])


def save_csv(data):
    columns = ["country", "year", "population"]

    with open(
        OUTPUT_FILE, "w", newline="", encoding="utf-8-sig"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(data)


def main():
    data = collect_population()
    save_csv(data)

    print("So ban ghi thu thap:", len(data))
    print("File da luu:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
