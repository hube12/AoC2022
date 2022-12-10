from typing import Tuple, List, Annotated

Point = Annotated[List[int], 2]


def sign(x):
    return (x > 0) - (x < 0)

def move_tail_element(e1: Point, e2: Point):
    x_d = e1[0] - e2[0]
    y_d = e1[1] - e2[1]
    if abs(x_d) > 1 or abs(y_d) > 1:
        e2[0] += sign(x_d)
        e2[1] += sign(y_d)


def move_head(h: Point, direction: str):
    h[0] += 1 if direction == 'R' else -1 if direction == 'L' else 0
    h[1] += 1 if direction == 'D' else -1 if direction == 'U' else 0


def move(rope: List[Point], direction: str) -> Tuple[int, int]:
    move_head(rope[0], direction)
    for i in range(1, len(rope)):
        move_tail_element(rope[i - 1], rope[i])
    return tuple(rope[-1])


for rope_length in [2, 10]:
    rope = [[0, 0] for _ in range(rope_length)]
    visited = set()
    for line in open("../../Downloads/input22_9.txt"):
        direction, steps = line.strip().split()
        assert (steps.isdigit())
        for _ in range(int(steps)):
            visited.add(move(rope, direction))
    print("Visited", len(visited))
