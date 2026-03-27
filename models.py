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
   def __str__(self):
        return f"{self.name} - {self.code} - Goals: {self.goals} - Assists: {self.assists}"


class GoalPoacher(SquadMember):
    def __init__(self, name, code, email, shots=0):
        super().__init__(name, code, email)
        self.shots = shots

    def record_shot(self):
        self.shots = self.shots + 1

    def pack(self):
        data = super().pack()
        data["role"] = "GoalPoacher"
        data["extra"] = self.shots
        return data

    def __str__(self):
        return super().__str__() + f" - Shots: {self.shots}"


class ClubRegister:
    def __init__(self):
        self.entries = []

    def insert(self, member):
        for current in self.entries:
            if current.code == member.code:
                raise ValueError("That player code already exists")
        self.entries.append(member)

    def fetch(self, code):
        for current in self.entries:
            if current.code == code:
                return current
        return None

    def erase(self, code):
        for i in range(len(self.entries)):
            if self.entries[i].code == code:
                self.entries.pop(i)
                return True
        return False

    def listing(self):
        return self.entries  