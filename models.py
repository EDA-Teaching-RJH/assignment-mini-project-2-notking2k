class Player:
    def __init__(self, name, player_id, email):
        self.name = name
        self.player_id = player_id
        self.email = email
        self.goals = 0
        self.assists = 0
from validators import clean_name, check_player_id, check_email

class Player:
    def __init__(self, name, player_id, email):
        self.name = clean_name(name)

        if not check_player_id(player_id):
            raise ValueError("Invalid ID")
        self.player_id = player_id

        if not check_email(email):
            raise ValueError("Invalid email")
        self.email = email

        self.goals = 0
        self.assists = 0        
    def add_goal(self):
        self.goals += 1

    def add_assist(self):
        self.assists += 1   
    def __str__(self):
        return f"{self.name} ({self.player_id}) - Goals: {self.goals}"    

class Striker(Player):
    def __init__(self, name, player_id, email):
        super().__init__(name, player_id, email)
        self.shots = 0    
class Team:
    def __init__(self):
        self.players = []        