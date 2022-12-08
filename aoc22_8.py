import enum
import time
from typing import List, Set, Tuple, Union


class Axis(enum.Enum):
    Y_AXIS = 0
    X_AXIS = 1


class Direction(enum.Enum):
    NORMAL = 0
    INVERTED = 1


def filter_side(forest: List[List[int]], is_visible: Set[Tuple[int, int]], axis_bound: int, side_pos: int,
                flood_range: Union[range, reversed], axis: Axis):
    is_currently_visible = dict()
    for axis_it in range(axis_bound):
        is_visible.add((axis_it, side_pos) if axis == Axis.Y_AXIS else (side_pos, axis_it))
        is_currently_visible[axis_it] = forest[axis_it][side_pos] if axis == Axis.Y_AXIS else forest[side_pos][axis_it]
    for flood_it in flood_range:
        for axis_it, k in is_currently_visible.items():
            current = forest[axis_it][flood_it] if axis == Axis.Y_AXIS else forest[flood_it][axis_it]
            if current > k:
                is_currently_visible[axis_it] = current
                is_visible.add((axis_it, flood_it) if axis == Axis.Y_AXIS else (flood_it, axis_it))
        is_currently_visible = {k: v for k, v in is_currently_visible.items() if v < 9}


def ray(forest: List[List[int]], pos: Tuple[int, int], axis: Axis, direction: Direction):
    """
    Cast a ray until a tree if the same height or taller
    :param forest:
    :param pos: Should be (y,x)
    :param axis:
    :param direction:
    :return: the length of the ray
    """
    length = len(forest[0])
    height = len(forest)
    y = pos[0]
    x = pos[1]
    tree = forest[y][x]
    counter = 0
    while True:
        amount = 1 if direction == Direction.NORMAL else -1
        if axis == Axis.Y_AXIS:
            y += amount
        else:
            x += amount
        if x not in range(0, length) or y not in range(0, height):
            break
        if forest[y][x] >= tree:
            counter += 1
            break
        counter += 1
    return counter

with open("../../Downloads/input22_8.txt") as f:
    forest = []
    for line in f:
        line = line.strip()
        forest.append(list(map(int, list(line))))
    length = len(forest[0])
    height = len(forest)
    is_visible = set()
    ## Right side
    filter_side(forest, is_visible, height, length - 1, reversed(range(0, length - 1)), Axis.Y_AXIS)
    ## Left side
    filter_side(forest, is_visible, height, 0, range(1, length), Axis.Y_AXIS)
    ## Top side
    filter_side(forest, is_visible, length, 0, range(1, height), Axis.X_AXIS)
    ## Bottom side
    filter_side(forest, is_visible, length, height - 1, reversed(range(0, height - 1)), Axis.X_AXIS)
    if 1:
        for y in range(height):
            for x in range(length):
                print(forest[y][x] if (y, x) in is_visible else ".", end="")
            print()
    print()
    print(len(is_visible))
    print()
    max_score = 0
    for y in range(1, height - 1):
        for x in range(1, length - 1):
            ray_down = ray(forest, (y, x), Axis.Y_AXIS, Direction.NORMAL)
            ray_up = ray(forest, (y, x), Axis.Y_AXIS, Direction.INVERTED)
            ray_right = ray(forest, (y, x), Axis.X_AXIS, Direction.NORMAL)
            ray_left = ray(forest, (y, x), Axis.X_AXIS, Direction.INVERTED)
            score = ray_left * ray_up * ray_down * ray_right
            max_score = max(score, max_score)
    print(max_score)