import re


def normalise_name(value):
    value = re.sub(r"[^A-Za-z\s]", "", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip().title()

def player_code_ok(value):
    pattern = r"^PLR\d{4}$"
    return re.match(pattern, value) is not None

def email_ok(value):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.fullmatch(pattern, value) is not None
