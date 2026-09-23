from src.reader import reader
from src.check_for_nulls import check_for_nulls
from src.clean_data import clean_data
from src.processed import processed
from src.check_for_duplicates import check_for_duplicates
from pathlib import Path

current_directory = Path(__file__).resolve().parent
output_dir = current_directory.parent / "data" / "processed"
data_dir = current_directory.parent / "data" / "raw"
output_dir.mkdir(parents=True, exist_ok=True)


def main():
    dataset = reader(data_dir)
    null = check_for_nulls(dataset)
    duplicates = check_for_duplicates(null)
    clean = clean_data(duplicates)

    
    processed(output_dir, duplicates)


if __name__ == "__main__":
    main()