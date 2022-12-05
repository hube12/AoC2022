import string

with open("../Downloads/input22_3.txt") as f:
    score = 0
    for line in f:
        line = line.strip()
        assert len(line) % 2 == 0
        mid = len(line) // 2
        first_half, second_half = set(line[:mid]), set(line[mid:])
        common = first_half & second_half
        assert len(common) == 1
        score += string.ascii_letters.index(common.pop()) + 1
    print(score)

    f.seek(0)

    score = 0
    lines = [map(lambda x: x.strip(), iter(f))] * 3
    for group in zip(*lines):
        assert len(group) > 0
        s = set(group[0])
        for line in group[1:]:
            s &= set(line)
        assert len(s) == 1
        score += string.ascii_letters.index(s.pop()) + 1
    print(score)
