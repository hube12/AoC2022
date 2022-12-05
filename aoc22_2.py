rules1 = {
    "X": (1, {"A": 3, "B": 0, "C": 6}),
    "Y": (2, {"A": 6, "B": 3, "C": 0}),
    "Z": (3, {"A": 0, "B": 6, "C": 3}),
}

rules2 = {
    "X": (0, {"A": 3, "B": 1, "C": 2}),
    "Y": (3, {"A": 1, "B": 2, "C": 3}),
    "Z": (6, {"A": 2, "B": 3, "C": 1}),
}
with open("../Download/input22_2.txt") as f:
    turns = []
    score1 = 0
    score2 = 0
    for line in f:
        elf, you = line.strip().split()
        turns.append((elf, you))
        turn_rule1 = rules1[you]
        turn_rule2 = rules2[you]
        score1 += turn_rule1[0] + turn_rule1[1][elf]
        score2 += turn_rule2[0] + turn_rule2[1][elf]
    print(score1)
    print(score2)
