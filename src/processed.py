import csv
def processed(output_dir, dataset):
    try: 
        with open(f"{output_dir}/fifa21_raw_data.csv", "w",newline="", encoding="utf-8") as f:
            fields = []
            for key in dataset[0].keys():
                fields.append(key)
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(dataset)
        print("Data processed with success!")
    except Exception as e:
        print("Something error occurred: ", e)