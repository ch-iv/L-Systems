class System:
    def __init__(self, axiom: str, rules: dict, constants=None):

        self.axiom = axiom
        self.rules = rules

        if constants is None:
            self.constants = set()
        else:
            self.constants = constants

    def advance(self, steps: int):
        new_axiom = self.axiom

        for _ in range(steps):
            buffer = ""
            for char in new_axiom:
                if char in self.constants:
                    buffer += char
                else:
                    buffer += self.rules[char]
            new_axiom = buffer

        return new_axiom
