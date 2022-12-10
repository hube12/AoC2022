cycle = 1
value = 1

total = 0

crt = [[""] * 40 for _ in range(6)]
print(len(crt))


def check_cycle_condition():
    global total
    if cycle in [20, 60, 100, 140, 180, 220]:
        total += cycle * value
    if cycle - 1 < len(crt) * len(crt[0]):
        vertical = (cycle - 1) // 40
        horizontal = (cycle - 1) % 40
        if abs(horizontal - value) < 2:
            crt[vertical][horizontal] = "#"
        else:
            crt[vertical][horizontal] = "."


for line in open("../../Downloads/input22_10.txt"):
    line = line.strip()
    if line.startswith("noop"):
        check_cycle_condition()
        cycle += 1
    else:
        op, arg = line.split()
        if op == "addx":
            if arg[0] in ["+", "-"]:
                assert (arg[1:].isdigit())
            else:
                assert (arg.isdigit())
            check_cycle_condition()
            cycle += 1
            check_cycle_condition()
            cycle += 1
            value += int(arg)
print(total)
print("\n".join(["".join(c) for c in crt]))
