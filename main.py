import argparse

from src.candidate_loader import split_candidates
from src.csv_io import read_rows, write_valid, write_errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()
    rows = read_rows(args.input_file)

    good, bad = split_candidates(rows)

    write_valid('valid.csv', good)
    write_errors('errors.csv', bad)

    print(len(good), len(bad))


if __name__ == "__main__":
    main()