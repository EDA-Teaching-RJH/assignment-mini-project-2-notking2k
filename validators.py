import re


def normalise_name(value):
    value = re.sub(r"[^A-Za-z\s]", "", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip().title()

