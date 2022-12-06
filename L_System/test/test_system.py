from L_System import System


def test_algae():
    axiom = "A"
    rules = {"A": "AB", "B": "A"}

    system = System(axiom=axiom, rules=rules)

    assert system.advance(0) == "A"
    assert system.advance(1) == "AB"
    assert system.advance(2) == "ABA"
    assert system.advance(3) == "ABAAB"
    assert system.advance(4) == "ABAABABA"
    assert system.advance(5) == "ABAABABAABAAB"
    assert system.advance(6) == "ABAABABAABAABABAABABA"
    assert system.advance(7) == "ABAABABAABAABABAABABAABAABABAABAAB"


def test_binary_tree():
    axiom = "0"
    rules = {"1": "11", "0": "1[0]0"}
    constants = {"[", "]"}

    system = System(axiom=axiom, rules=rules, constants=constants)

    assert system.advance(0) == "0"
    assert system.advance(1) == "1[0]0"
    assert system.advance(2) == "11[1[0]0]1[0]0"
    assert system.advance(3) == "1111[11[1[0]0]1[0]0]11[1[0]0]1[0]0"


def test_cantor_set():
    axiom = "A"
    rules = {"A": "ABA", "B": "BBB"}

    system = System(
        axiom=axiom,
        rules=rules,
    )

    assert system.advance(0) == "A"
    assert system.advance(1) == "ABA"
    assert system.advance(2) == "ABABBBABA"
    assert system.advance(3) == "ABABBBABABBBBBBBBBABABBBABA"


def test_koch_curve():
    axiom = "F"
    rules = {"F": "F+F-F-F+F"}
    constants = {"+", "-"}

    system = System(axiom=axiom, rules=rules, constants=constants)

    assert system.advance(0) == "F"
    assert system.advance(1) == "F+F-F-F+F"
    assert system.advance(2) == "F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F"
