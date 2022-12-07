import os
from typing import NamedTuple, List, Optional, Callable, Any
from pathlib import PurePosixPath, PurePosixPath
from functools import lru_cache


class Node:
    def __init__(self, path: PurePosixPath, size: int, children: List['Node'], parent: Optional['Node']):
        self.path = path
        self.size = size
        self.children = children
        self.parent = parent

    def insert(self, path: PurePosixPath, size: int) -> bool:
        current = self.get_root()
        for parent in reversed(path.parents):
            if parent.root == str(parent):
                continue
            found = False
            for child in current.children:
                if str(child.path) == str(parent):
                    current = child
                    found = True
            if not found:
                return False
        current.children.append(Node(path, size, [], current))
        return True

    @lru_cache(2048)
    def get_size(self):
        size = self.size
        for child in self.children:
            size += child.get_size()
        return size

    def dfs(self, f: Callable[['Node', Any], None], acc: Any):
        for children in self.children:
            f(children, acc)
            children.dfs(f, acc)

    def get_root(self):
        if self.parent is not None:
            return self.parent.get_root()
        return self


def simplifyPath(path):
    stack, tokens = [], path.split("/")
    for token in tokens:
        if token == ".." and stack:
            stack.pop()
        elif token != ".." and token != "." and token:
            stack.append(token)
    return "/" + "/".join(stack)


def filter1(node, acc):
    if len(node.children):
        size = node.get_size()
        if size < 100000:
            acc[0] += size


def filter2(node, acc, to_free):
    if len(node.children):
        size = node.get_size()
        if size > to_free:
            if size < acc[0]:
                acc[0] = size


with open("../../Downloads/input22_7.txt") as f:
    filesystem = Node(PurePosixPath("/"), 0, [], None)
    current_cwd = None
    is_listing = False
    for line in f:
        line = line.strip()
        if line.startswith("$ "):
            is_listing = False
            # command
            line = line[2:]
            if line.startswith("cd "):
                path = line[3:]
                if current_cwd is None:
                    current_cwd = PurePosixPath(path)
                else:
                    current_cwd /= path
                current_cwd = PurePosixPath(simplifyPath(current_cwd.as_posix()))
            elif line.startswith("ls"):
                is_listing = True
            else:
                raise Exception("Not a valid command")
        elif is_listing:
            size, name = line.split(" ")
            if size == "dir":
                size = 0
            else:
                assert (size.isdigit())
            if not filesystem.insert((PurePosixPath(current_cwd) / name), int(size)):
                print(line)
        else:
            raise Exception("Not a command, nor a list, GIGO")
    acc = [0]
    filesystem.dfs(lambda node, acc: filter1(node, acc), acc)
    print("Files under 100000 makes up", acc[0])
    full_size = filesystem.get_size()
    free_space = 70000000 - full_size
    assert (free_space > 0)
    if free_space < 30000000:
        to_free = 30000000 - free_space
        acc = [70000000]
        filesystem.dfs(lambda node, acc: filter2(node, acc, to_free), acc)
        print("Free at least", acc[0])
    else:
        print("No need to free")
