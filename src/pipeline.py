import  json
import csv
from pathlib import Path

current_directory = Path(__file__).resolve().parent
output_dir = current_directory.parent / "data" / "processed"
data_dir = current_directory.parent / "data" / "raw"
output_dir.mkdir(parents=True, exist_ok=True)

files = [
    "fifa21_raw_data",
    "fifa21 raw data v2"
]

datasets = {}

for file_name in files:
    with open(f"{data_dir}/{file_name}.csv", "r", encoding="utf-8") as f:
        datasets[file_name] = list(csv.DictReader(f))
    with open(f"{output_dir}/{file_name}.json", "w", encoding="utf-8") as f:
        json.dump(datasets[file_name], f, indent=2)

def check_for_nulls(dataset):
    for file_name in files:
        with open(f"{output_dir}/{file_name}.json", "r", encoding="utf-8") as f:
            json_file = json.load(f)
            for record in json_file:
                for field, value in record.items():
                    if value is None:
                        record.pop(field)


check_for_nulls(datasets)
