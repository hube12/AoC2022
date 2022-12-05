#!/bin/python3
import itertools
import sys
from collections import defaultdict

MIN_PYTHON = (3, 10)
if sys.version_info < MIN_PYTHON:
    sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)

with open("../Downloads/input22_5.txt") as f:
    crates1 = defaultdict(list)
    crates2 = defaultdict(list)
    move = False
    for line in f:
        line = line.strip("\n")
        if line == "":
            move = True
            continue
        if move:
            elements = line.split(" ")
            assert elements[0] == "move"
            assert elements[1].isdigit()
            assert elements[2] == "from"
            assert elements[3].isdigit()
            assert elements[4] == "to"
            assert elements[5].isdigit()

            count = int(elements[1])
            src = int(elements[3])
            dst = int(elements[5])
            assert len(crates1[src]) >= count
            assert len(crates2[src]) >= count
            for _ in range(count):
                crates1[dst].insert(0, crates1[src].pop(0))
            extracted = crates2[src][:count]
            crates2[src] = crates2[src][count:]
            extracted.extend(crates2[dst])
            crates2[dst] = extracted
            pass
        else:
            # parse the crates
            it = iter(list(line))
            crate = 1
            while True:
                it.__next__()
                letter = it.__next__()
                it.__next__()
                if letter != " " and not letter.isdigit():
                    crates1[crate].append(letter)
                    crates2[crate].append(letter)
                # burn space or exit
                if next(it, None) is None:
                    crate = 1
                    break
                crate += 1
    for i in range(len(crates1)):
        print(crates1[i + 1][0], end="")
    print()
    for i in range(len(crates2)):
        print(crates2[i + 1][0], end="")
