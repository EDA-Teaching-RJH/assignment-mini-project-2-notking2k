for row in reader:
            if row["type"] == "Striker":
                player = Striker(row["name"], row["player_id"], row["email"], int(row["extra"]))
            else:
                player = Player(row["name"], row["player_id"], row["email"])

            player.goals = int(row["goals"])
            player.assists = int(row["assists"])
            team.players.append(player)
def log_action(text, file_name="activity_log.txt"):
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f"{now} - {text}\n") 