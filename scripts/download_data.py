import kagglehub
from kagglehub import KaggleDatasetAdapter
from pathlib import Path
import os

def main():
    # Set the path to the file you'd like to load
    current_directory = Path(__file__).resolve().parent
    Path(f"{current_directory.parent}/data/").mkdir(parents=True, exist_ok=True)
    file_path = current_directory.parent / "data" / "raw"


    # Load the latest version
    try:
        kagglehub.dataset_download(
            "yagunnersya/fifa-21-messy-raw-dataset-for-cleaning-exploring",
            path="fifa21_raw_data.csv",
            output_dir=str(file_path),
        )
        if os.path.getsize(f"{file_path}/fifa21_raw_data.csv") == 0 :
            print("File is empty")
    except Exception as e:
        print("Error while installing data:", e)

if __name__ == "__main__":
    main()