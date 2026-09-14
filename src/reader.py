import csv
def reader(data_dir):
    files = [
        "fifa21_raw_data",
        "fifa21 raw data v2"
    ]

    datasets = {}

    for file_name in files:
        with open(f"{data_dir}/{file_name}.csv", "r", encoding="utf-8") as f:
            datasets[file_name] = list(csv.DictReader(f))
        
    print("WORKED!")

    return datasets