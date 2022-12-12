import sys

board = {}
for i, line in enumerate(open("../../Downloads/input22_12.txt")):
    line = line.strip()
    for j, c in enumerate(line):
        board[(i, j)] = c

S = next(pos for pos, v in board.items() if v == 'S')
E = next(pos for pos, v in board.items() if v == 'E')


def findPath(start, next_step_pred, path_done_pred):
    queue = [[start]]
    shortest_len = sys.maxsize
    visited = {start}
    while queue:
        current_queue, queue = queue, []
        for path in current_queue:
            pos = path[-1]
            for step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                npos = (pos[0] + step[0], pos[1] + step[1])
                if npos in board and npos not in visited and next_step_pred(board[pos], board[npos]):
                    if path_done_pred(npos):
                        shortest_len = min(shortest_len, len(path) + 1)
                    visited.add(npos)
                    queue.append(path + [npos])
    return shortest_len - 1


print(findPath(S, lambda v, next_v: ord(next_v) <= ord(v) + 1 or v == 'S', lambda pos: pos == E))
print(findPath(E, lambda v, next_v: ord(v) <= ord(next_v) + 1, lambda pos: board[pos] == 'a' or pos == S))
