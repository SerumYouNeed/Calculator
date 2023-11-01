class account():
    def __init__(self, name = "user", password = 1234, score = 0, points = 0):
        self.name = name
        self.password = password
        self.score = score
        self.points = points

    def update_points(self, added):
        self.points += added

user = account()