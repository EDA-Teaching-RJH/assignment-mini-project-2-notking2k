# this file checks that the user input is in the correct format
import re

#this removes the symbols from a name and will tidy the spaces 
def clean_name(name):
    name = re.sub(r"[^A-Za-z\s]", "", name)
    return name.strip().title()
def clean_name(name):
    name = re.sub(r"[^A-Za-z\s]", "", name)
    name = re.sub(r"\s+", " ", name)
    return name.strip().title()
# this will check that the players id matches the correct from like PLR4567
def check_player_id(player_id):
    return re.match(r"^PLR\d{4}$", player_id) is not None
def check_email(email):
    return re.fullmatch(r"[\w\.-]+@[\w\.-]+\.\w+", email) is not None
def find_parts(text):
    return re.findall(r"[A-Za-z0-9]+", text)