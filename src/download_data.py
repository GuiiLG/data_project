import kagglehub
from kagglehub import KaggleDatasetAdapter
from pathlib import Path

# Set the path to the file you'd like to load
current_directory = Path(__file__).resolve().parent
file_path = current_directory.parent / "data" / "raw"


# Load the latest version
for file_name in [
    "olist_customers_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_orders_dataset.csv",
    "olist_products_dataset.csv",
    "product_category_name_translation.csv"
]:
    kagglehub.dataset_download(
        "olistbr/brazilian-ecommerce",
        path=file_name,
        output_dir=str(file_path),
    )

