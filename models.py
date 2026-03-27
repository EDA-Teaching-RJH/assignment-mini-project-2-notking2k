from validators import normalise_name, player_code_ok, email_ok
class SquadMember:
    def __init__(self, name, code, email):
        self.name = normalise_name(name)

        if not player_code_ok(code):
            raise ValueError("Player code is not valid")
        self.code = code

        if not email_ok(email):
            raise ValueError("Email is not valid")
        self.email = email

        self.goals = 0
        self.assists = 0

    def record_goal(self):
        self.goals = self.goals + 1

    def record_assist(self):
        self.assists = self.assists + 1

    def pack(self):
        return {
            "name": self.name,
            "code": self.code,
            "email": self.email,
            "goals": self.goals,
            "assists": self.assists,
            "role": "SquadMember",
            "extra": ""
        }