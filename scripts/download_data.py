import kagglehub
from kagglehub import KaggleDatasetAdapter
from pathlib import Path

# Set the path to the file you'd like to load
current_directory = Path(__file__).resolve().parent
file_path = current_directory.parent / "data" / "raw"


# Load the latest version
try:
    kagglehub.dataset_download(
        "yagunnersya/fifa-21-messy-raw-dataset-for-cleaning-exploring",
        path="fifa21_raw_data.csv",
        output_dir=str(file_path),
    )
except Exception as e:
    print("Error while installing data:", e)

