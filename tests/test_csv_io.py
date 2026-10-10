from src.csv_io import read_rows


def test_read_rows(tmp_path):
    csv_content = "name,email,experience\nJohn Doe,john@example.com,5\nJane Smith,jane@example.com,10"
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content, encoding='utf-8')
    rows = read_rows(str(csv_file))
    assert len(rows) == 2
    assert rows[0] == {"name": "John Doe", "email": "john@example.com", "experience": "5"}