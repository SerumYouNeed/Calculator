class account():
    def __init__(self, name = "user", score = 0):
        self.name = name
        self.score = score

    def update_score(self, added): 
        self.score += added

player = account()