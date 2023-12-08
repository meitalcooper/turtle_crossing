from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("black")
        self.hideturtle()
       
    
    def update_scoreboard(self):
        """the scoreboard keeps track of which level the user is on."""
        self.clear()
        self.goto(-220,250)
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

   
    def game_over(self):
        """When the turtle hits a car, GAME OVER displayed in the centre."""
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
            
    def increase_score(self):
        """Every time the turtle player does a successful crossing, the level increase."""
        self.score +=1
        self.clear()
        self.update_scoreboard()

