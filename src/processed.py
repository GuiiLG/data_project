import csv
def processed(output_dir, datasets):
    with open(f"{output_dir}/fifa21_raw_data.csv", "w", encoding="utf-8") as f:
        fields = []
        for key in datasets["fifa21_raw_data"][0].keys():
            fields.append(key)
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(datasets["fifa21_raw_data"])