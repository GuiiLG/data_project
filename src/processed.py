import csv
def processed(output_dir, dataset):
    with open(f"{output_dir}/fifa21_raw_data.csv", "w", encoding="utf-8") as f:
        fields = []
        for key in dataset[0].keys():
            fields.append(key)
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(dataset)