import re
def clean_name(name):
    name = re.sub(r"[^A-Za-z\s]", "", name)
    return name.strip().title()
def clean_name(name):
    name = re.sub(r"[^A-Za-z\s]", "", name)
    name = re.sub(r"\s+", " ", name)
    return name.strip().title()