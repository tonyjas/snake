from turtle import Turtle


class ScoreBoard(Turtle):

    score = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.goto(0, 280)
        self.refresh_score()

    def update_score(self):
        self.score += 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align="center")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = -1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", False, align="center")
