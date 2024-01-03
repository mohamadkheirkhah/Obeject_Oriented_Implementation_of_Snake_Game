from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        try:
            with open('high_score.txt') as file:
                highest_score = file.read()
        except:
            with open('high_score.txt', 'w') as file:
                file.write(str(0))
            with open('high_score.txt', 'r') as file:
                highest_score = file.read()

        self.score = 0
        self.high_score = int(highest_score)
        self.penup()
        self.color('white')
        self.goto(0, 280)
        self.hideturtle()
        self.write(arg=f'Score: {self.score}  High Score: {self.high_score} ', align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        if self.score >= int(self.high_score):
            self.high_score += 1
            with open('high_score.txt', 'w') as writer:
                writer.write(str(self.high_score))

        self.score += 1
        self.write(arg=f'Score: {self.score}  High Score: {self.high_score} ', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over!', align=ALIGNMENT, font=FONT)


