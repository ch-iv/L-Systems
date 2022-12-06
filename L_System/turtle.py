import turtle
from enum import Enum
#
#




class LTurtle(turtle.Turtle):
    FORWARD = "LTurtle.Forward"
    LEFT = "LTurtle.Left"
    RIGHT = "LTurtle.Left"
    SAVE_POSITION = "LTurtle.SavePosition"
    POP_POSITION = "LTurtle.PopPosition"
    PASS = "LTurtle.Pass"

    def __init__(self, WIDTH: float, HEIGHT: float):
        super().__init__()
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.actions = None
        self.saved_positions = []

        screen = turtle.Screen()
        screen.setup(self.WIDTH, self.HEIGHT)
        screen.delay(0)
        screen.tracer(0, 0)

        self.screen = screen
        self.penup()
        self.pendown()
        self.color("black")
        self.pensize(3)

    def set_actions(self, actions: dict):
        self.actions = actions

    def draw_axiom(self, axiom: str):
        for char in axiom:
            action = self.actions[char]
            match action:
                case LTurtle.FORWARD:
                    self.forward(10)
                case LTurtle.LEFT:
                    self.left(10)
                case LTurtle.RIGHT:
                    self.right(10)
                case LTurtle.SAVE_POSITION:
                    self.saved_positions.append([turtle.xcor(), turtle.ycor(), turtle.heading()])
                case LTurtle.POP_POSITION:
                    self.penup()
                    last_position = self.saved_positions.pop(-1)
                    self.setx(last_position[0])
                    self.sety(last_position[1])
                    self.setheading(last_position[2])
                    self.pendown()
                case LTurtle.PASS:
                    pass
                case _:
                    raise Exception(f"Unknown action {action}")




