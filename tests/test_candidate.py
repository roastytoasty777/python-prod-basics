import pytest
from src.candidate import Candidate
from pydantic import ValidationError


@pytest.mark.parametrize("name, email, experience, skills", [
    ("Test", "test@example.com", 0, []),
])
def test_candidate_creation(name, email, experience, skills):
    candidate = Candidate(name=name, email=email, experience=experience, skills=skills)
    assert candidate.name == name
    assert candidate.email == email
    assert candidate.experience == experience
    assert candidate.skills == skills


def test_candidate_default_skills():
    candidate = Candidate(name="Test", email="test@example.com", experience=0)
    assert candidate.skills == []


def test_candidate_invalid_email():
    with pytest.raises(ValidationError):
        Candidate(name="Test", email="invalid-email", experience=0)


def test_candidate_negative_experience():
    with pytest.raises(ValidationError):
        Candidate(name="Test", email="test@example.com", experience=-1)


def test_candidate_missing_name():
    with pytest.raises(ValidationError):
        Candidate(email="test@example.com", experience=0) # type: ignore