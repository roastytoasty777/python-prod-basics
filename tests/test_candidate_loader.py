from src.candidate_loader import split_candidates


def test_split_candidates():
    items = [
        {"name": "Test", "email": "test@example.com", "experience": 0, "skills": []},
        {"name": "Sami", "email": "invalid-email", "experience": 0, "skills": []},
        {"name": "John", "email": "john@example.com", "experience": 5, "skills": ["Python", "Java"]},
        {"name": "Alice", "email": "alice@example.com", "experience": -1, "skills": ["JavaScript", "TypeScript"]}
    ]
    good, bad = split_candidates(items)
    assert len(good) == 2
    assert len(bad) == 2
    assert good[0].name == "Test"
    assert bad == [
        {"name": "Sami", "email": "invalid-email", "experience": 0, "skills": []},
        {"name": "Alice", "email": "alice@example.com", "experience": -1, "skills": ["JavaScript", "TypeScript"]}
    ]