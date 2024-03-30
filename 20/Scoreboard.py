from turtle import Turtle

ALIGMENT = "center"
FONT = "Arial"

class Scoreboard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.load_high_score()
        self.setposition(0,260)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:  {self.score}   High Score: {self.high_score}", align= ALIGMENT, font=(FONT, 16, "normal"))  

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        self.save_high_score()
    
    def refresh(self):
        self.score += 1
        self.update_scoreboard()


    def save_high_score(self):
        with open("20/high_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def load_high_score(self):
        with open("20/high_score.txt", mode="w") as file:
            pass
        with open("20/high_score.txt", mode="r") as file:
            self.high_score = file.read()
        if self.high_score == None or self.high_score == "":
            self.high_score = 0
        else: 
            self.high_score = int(self.high_score)