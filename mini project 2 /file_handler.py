#this file sorts out the process of saving, loading and logging the data 
import csv
#this allows me to save all the players into the csv file so data isnt lost 
def save_players(team):
    with open("players.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "id", "email"])
    for p in team.players:
        writer.writerow([p.name, p.player_id, p.email])       
#then load them back from the csv file 
def    load_players(team):
    with open("players.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)