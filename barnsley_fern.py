from L_System import LTurtle
from L_System import System

axiom = "X"
rules = {"F": "FF", "X": "F+[[X]-X]-F[-FX]+X", "+": "+", "-": "-", "[": "[", "]": "]"}
actions = {
    "F": LTurtle.FORWARD,
    "+": LTurtle.LEFT,
    "-": LTurtle.RIGHT,
    "[": LTurtle.SAVE_POSITION,
    "]": LTurtle.POP_POSITION,
    "X": LTurtle.PASS,
}

system = System(axiom=axiom, rules=rules)

HEIGHT = 1000.0
WIDTH = 1500.0

lturtle = LTurtle(WIDTH, HEIGHT)
lturtle.set_actions(actions)
lturtle.draw_axiom(system.advance(6))
lturtle.screen.mainloop()
