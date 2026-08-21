import re

def normalize_plate(plate: str) -> str:
    if not plate:
        return ""

    text = plate.upper()
    text = text.replace("-", "")
    text = text.replace(" ", "")

    match = re.match(r"([A-Z]{1,3})([A-Z]{1,3})(\\d+)", text)

    if match:
        city, letters, number = match.groups()
        return f"{city}-{letters} {number}"

    return plate.upper().strip()