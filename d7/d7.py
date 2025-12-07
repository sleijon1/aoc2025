from functools import lru_cache

rows = list(map(list, open("input.txt").read().splitlines()))
starting_point = None
for i, row in enumerate(rows):
    for j, point in enumerate(row):
        if point == "S":
            starting_point = (j, i)
            break
splitters = set()


@lru_cache(maxsize=None)
def quantum_beam(point):
    global splitters
    x, y = point
    if y + 1 < len(rows):
        if rows[y + 1][x] == "^":
            splitters.add((x, y + 1))
            return quantum_beam((x + 1, y + 1)) + quantum_beam((x - 1, y + 1))
        else:
            return quantum_beam((x, y + 1))
    return 1


timelines = quantum_beam(starting_point)


print(f"p1: {len(splitters)}, p2: {timelines}")
