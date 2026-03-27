import re
def clean_name(name):
    name = re.sub(r"[^A-Za-z\s]", "", name)
    return name.strip().title()
def clean_name(name):
    name = re.sub(r"[^A-Za-z\s]", "", name)
    name = re.sub(r"\s+", " ", name)
    return name.strip().title()
def check_player_id(player_id):
    return re.match(r"^PLR\d{4}$", player_id) is not None