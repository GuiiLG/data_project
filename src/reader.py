import csv
def reader(data_dir):
    file_name = "fifa21_raw_data"
    try:
        with open(f"{data_dir}/{file_name}.csv", "r", encoding="utf-8") as f:
            dataset= list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"File not found: {data_dir}/{file_name}.csv")
    return dataset