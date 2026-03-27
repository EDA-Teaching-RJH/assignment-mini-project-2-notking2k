def top_scorer(team):
    if len(team.players) == 0:
        return None

    best = team.players[0]

    for player in team.players:
        if player.goals > best.goals:
            best = player

    return best


def total_goals(team):
    total = 0
    for player in team.players:
        total += player.goals
    return total


def total_assists(team):
    total = 0
    for player in team.players:
        total += player.assists
    return total


def average_goals(team):
    if len(team.players) == 0:
        return 0
    return total_goals(team) / len(team.players)