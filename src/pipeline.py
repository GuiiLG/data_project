import  json
import csv
from pathlib import Path

current_directory = Path(__file__).resolve().parent
output_dir = current_directory.parent / "data" / "processed"
data_dir = current_directory.parent / "data" / "raw"
output_dir.mkdir(parents=True, exist_ok=True)

files = [
    "olist_customers_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_orders_dataset.csv",
    "olist_products_dataset.csv",
    "product_category_name_translation.csv"
]

all_files = {}

for file_name in files:
    with open(f"{data_dir}/{file_name}", "r", encoding="utf-8") as f:
        file_name_no_csv = file_name.replace(".csv", "")
        all_files[file_name_no_csv] = list(csv.DictReader(f))
    with open(f"{output_dir}/{file_name_no_csv}.json", "w", encoding="utf-8") as f:
        json.dump(all_files[file_name_no_csv], f, indent=2)
