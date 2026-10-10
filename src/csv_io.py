import csv
from src.candidate import Candidate


def read_rows(path: str) -> list[dict]:
    with open(path, newline='', encoding='utf-8') as file:
        return list(csv.DictReader(file))


def write_valid(path: str, candidates: list[Candidate]) -> None:
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "email", "experience"], extrasaction='ignore')
        writer.writeheader()
        for candidate in candidates:
            writer.writerow(candidate.model_dump())


def write_errors(path: str, errors: list[dict]) -> None:
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "email", "experience"])
        writer.writeheader()
        for data in errors:
            writer.writerow(data)