from turtle import Turtle

class S_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.color("white")
        with open(r"D:\Career\Python\Python-Projects\Snake Game\data.txt") as data:
            high_score_str = data.read()
            if high_score_str:
                self.high_score = int(high_score_str)
        self.goto(0,270)
        #self.write(f"Score: {self.score}",align= "center", font = ("Arial",24,"normal"))
        self.hideturtle()
        self.update_board()
    
    def update_board(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}",align= "center", font = ("Arial",24,"normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(str(self.high_score))
        self.update_board()

    def reset_score(self):
        self.score = 0
        self.update_board()

    #def game_over(self):
    #    self.goto(0,0)
    #    self.write("GAME OVER!!!", align = "center", font=("Arial",24,"normal"))