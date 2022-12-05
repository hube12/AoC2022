import os
from operator import itemgetter

print(os.getcwd())
elfs = []
with open("../Download/input22_1.txt") as f:
    current_elf = []
    for line in f:
        line = line.strip()
        if not line:
            elfs.append(current_elf)
            current_elf = []
        else:
            current_elf.append(int(line))

print(max([(i, sum(x)) for i, x in enumerate(elfs)], key=itemgetter(1)))

print(sum(x[1] for x in sorted([(i, sum(x)) for i, x in enumerate(elfs)], key=itemgetter(1))[-3:]))
