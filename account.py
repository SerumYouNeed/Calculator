class account():
    def __init__(self, name = "user", password = 1234, score = 0):
        self.name = name
        self.password = password
        self.score = score

    def update_score(self, added): 
        self.score += added

user = account()