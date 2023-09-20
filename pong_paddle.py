from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        new_y1 = self.ycor() + 40
        self.goto(self.xcor(), new_y1)

    def down(self):
        new_y2 = self.ycor() - 40
        self.goto(self.xcor(), new_y2)
