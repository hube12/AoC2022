import functools
from dataclasses import dataclass
from typing import Callable, List

MONKEY = "Monkey "
ITEMS = "Starting items: "
OPERATION = "Operation: "
TEST = "Test: "
TEST_TRUE = "If true: "
TEST_FALSE = "If false: "
THROW = "throw to monkey "
DIVISIBLE = "divisible by "


@dataclass(frozen=False)
class Monkey:
    id: int
    items: List[int] = None
    operation: Callable[[int], int] = None
    test: Callable[[int], bool] = None
    action_true: int = None
    action_false: int = None
    divisor: int = None

    def is_set(self) -> bool:
        return self.items is not None and self.operation is not None and self.test is not None \
               and self.action_true is not None and self.action_false is not None and self.divisor is not None


def evaluate(s: str, x: int) -> int:
    s = s.replace("old", str(x))
    return eval(s)


def is_divisible(x: int, d: int) -> bool:
    return x % d == 0


monkeys = []
monkey_id = 0
current_monkey = Monkey(monkey_id)
for line in open("../../Downloads/input22_11.txt"):
    line = line.strip()
    if line == "":
        assert (current_monkey.is_set())
        monkeys.append(current_monkey)
        monkey_id += 1
        current_monkey = Monkey(monkey_id)
    else:
        if line.startswith(MONKEY):
            line = line[len(MONKEY):]
            assert (line.endswith(":"))
            line = line[:-1]
            assert (line.isdigit())
            current_id = int(line)
            assert (current_id == monkey_id)
        elif line.startswith(ITEMS):
            line = line[len(ITEMS):]
            items = line.split(", ")
            for it in items:
                assert (it.isdigit())
            current_monkey.items = list(map(int, items))
        elif line.startswith(OPERATION):
            line = line[len(OPERATION):]
            assigned, operations = line.split(" = ")
            assert (assigned == "new")
            ops = operations.split()
            # A no priority parser (really dumb)
            parsed_ops = []
            for i, cop in enumerate(ops):
                if i % 2 == 1:
                    if cop == "*":
                        op = lambda x, y: int.__mul__(x, y)
                    elif cop == "+":
                        op = lambda x, y: int.__add__(x, y)
                    else:
                        assert False
                else:
                    if cop == "old":
                        op = lambda x: x
                    else:
                        assert cop.isdigit()
                        op = lambda x, cop=cop: int(cop)
                parsed_ops.append(op)
            assert (len(parsed_ops) == 3)
            parsed_ops = tuple(parsed_ops)
            current_monkey.operation = lambda x, parsed_ops=parsed_ops: parsed_ops[1](parsed_ops[0](x),
                                                                                      parsed_ops[2](x))
        elif line.startswith(TEST):
            line = line[len(TEST):]
            if line.startswith(DIVISIBLE):
                line = line[len(DIVISIBLE):]
                assert line.isdigit()
                d = int(line)
                current_monkey.test = lambda x, d=d: is_divisible(x, d)
                current_monkey.divisor = d
            else:
                assert False
        elif line.startswith(TEST_TRUE):
            line = line[len(TEST_TRUE):]
            if line.startswith(THROW):
                line = line[len(THROW):]
                assert line.isdigit()
                current_monkey.action_true = int(line)
            else:
                assert False
        elif line.startswith(TEST_FALSE):
            line = line[len(TEST_FALSE):]
            if line.startswith(THROW):
                line = line[len(THROW):]
                assert line.isdigit()
                current_monkey.action_false = int(line)
            else:
                assert False
monkeys.append(current_monkey)

monkey_gcd = functools.reduce(lambda x, y: x * y, [monkey.divisor for monkey in monkeys])
monkey_items = {monkey.id: [*monkey.items] for monkey in monkeys}
for dont_worry, rounds in enumerate([20, 10000]):
    for monkey in monkeys:
        monkey.items = [*monkey_items[monkey.id]]
    monkey_item_count = [0] * len(monkeys)
    for i in range(rounds):
        for monkey in monkeys:
            items = monkey.items
            monkey.items = []
            for item in items:
                monkey_item_count[monkey.id] += 1
                new_item = monkey.operation(item)
                if not dont_worry:
                    new_item //= 3
                else:
                    new_item = new_item % monkey_gcd
                if monkey.test(new_item):
                    monkeys[monkey.action_true].items.append(new_item)
                else:
                    monkeys[monkey.action_false].items.append(new_item)
    print(monkey_item_count)
    monkey_item_count.sort(reverse=True)
    print(monkey_item_count[0] * monkey_item_count[1])
