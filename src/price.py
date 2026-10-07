def parse_price(text: str) -> float:
    cleaned = text.replace("DT", "").replace(",", ".").strip()
    return float(cleaned)