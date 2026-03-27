import csv
def save_players(team):
    with open("players.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "id", "email"])
    for p in team.players:
        writer.writerow([p.name, p.player_id, p.email])       