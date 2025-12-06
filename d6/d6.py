import operator
import re
from functools import reduce
from collections import defaultdict
_input = open("input.txt").read().split("\n")
op = {"*": operator.mul, "+": operator.add}
operators = re.findall(r'[+\*]', _input[-1])
p1, p2 = 0, 0
verticals = defaultdict(list)
p2_verticals = defaultdict(list)
for i, row in enumerate(_input[:-1]):
    for j, val in enumerate(map(int, re.findall(r'-?\d+', row))):
        verticals[j].append(val)
    for x in range(len(row)):
        try:
            p2_verticals[x].append(row[x])
        except ValueError:
            pass
new_verticals = []
new_vertical = []
for k, v in p2_verticals.items():
    if all(el == " " for el in v):
        new_verticals.append(new_vertical)
        new_vertical = []
        continue
    new_vertical.append(int("".join([el for el in v])))
new_verticals.append(new_vertical)

for o, v in enumerate(verticals.values()):
    p1 += reduce(op[operators[o]], v)

for o, v in enumerate(new_verticals):
    p2 += reduce(op[operators[o]], v)


print(f"p1: {p1}, p2: {p2}")
