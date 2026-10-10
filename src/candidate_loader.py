from src.candidate import Candidate
from pydantic import ValidationError


def split_candidates(items: list[dict]) -> tuple[list[Candidate], list[dict]]:
    valid_candidates = []
    rejected = []

    for data in items:
        try:
            valid_candidates.append(Candidate(**data))  # type: ignore
        except ValidationError:
            rejected.append(data)
    return valid_candidates, rejected
