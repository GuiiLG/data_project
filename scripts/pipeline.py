from src.reader import reader
from src.check_for_nulls import check_for_nulls
from src.clean_data import clean_data
from src.processed import processed
from pathlib import Path

current_directory = Path(__file__).resolve().parent
output_dir = current_directory.parent / "data" / "processed"
data_dir = current_directory.parent / "data" / "raw"
output_dir.mkdir(parents=True, exist_ok=True)


def main():
    datasets = reader(data_dir)
    clean = clean_data(datasets)
    processed(output_dir, clean)


if __name__ == "__main__":
    main()