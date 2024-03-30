from turtle import Turtle

ALIGMENT = "center"
FONT = "Arial"

class Scoreboard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.setposition(0,270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score:  {self.score}", align= ALIGMENT, font=(FONT, 16, "normal"))

    def refresh(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.setposition(0,0)
        self.write("GAME OVER", align= ALIGMENT, font=(FONT, 16, "normal"))
    