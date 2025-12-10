from itertools import combinations

tiles = [tuple(map(int, r.split(","))) for r in open("input.txt").read().split("\n")]

print("XQSD")
_map = [
    ["."] * (max([x[0] for x in tiles]) + 3)
    for _ in range(max(x[1] for x in tiles) + 3)
]
# for r in _map:
#    print("".join(r))
# print(len(_map), len(_map[0]))
print("lmao")
green_lines = set()
static_xs = set()
for (x1, y1), (x2, y2) in combinations(tiles, 2):
    x_range, y_range = x1, y1
    if y1 == y2:
        if x1 > x2:
            x_range = range(x2, x1 + 1)
        else:
            x_range = range(x1, x2 + 1)
    elif x1 == x2:
        if y1 > y2:
            y_range = range(y2, y1 + 1)
        else:
            y_range = range(y1, y2 + 1)
    else:
        continue
    green_lines.add((x_range, y_range))

green_tiles = set()

# for x, y in green_tiles:
#    _map[y][x] = "X"

for line in green_lines:
    if isinstance(line[0], range):
        for x in line[0]:
            _map[line[1]][x] = "X"
            green_tiles.add((x, line[1]))

    elif isinstance(line[1], range):
        for y in line[1]:
            _map[y][line[0]] = "X"
            green_tiles.add((line[0], y))

print("lol")
for y, row in enumerate(_map):
    try:
        xm = row.index("X")
        xe = len(row) - 1 - row[::-1].index("X")
        for x in range(xm, xe):
            _map[y][x] = "X"
            green_tiles.add(
                (x, y)
            )  # memory error but idk why i guess add ranges but seems weird
        if len(green_tiles) % 1000000 == 0:
            print("size:", len(green_tiles), "last:", x, y)

    except ValueError:
        continue


print(len(green_tiles))


p1, p2 = [], []


for (x1, y1), (x2, y2) in combinations(tiles, 2):
    p1.append(abs((x1 - x2 + 1) * (y1 - y2 + 1)))
    tile_in_space = False
    for tile in tiles:
        if tile != (x1, y1) and tile != (x2, y2):
            if (x1 < tile[0] < x2 or x2 < tile[0] < x1) and (
                y1 < tile[1] < y2 or y2 < tile[1] < y1
            ):
                tile_in_space = True
                break
    if not tile_in_space and (x1, y2) in green_tiles and (x2, y1) in green_tiles:
        p2.append(abs((x1 - x2 + 1) * (y1 - y2 + 1)))
        # if abs((x1 - x2 + 1) * (y1 - y2 + 1)) == 40:
        #    print((x1, y1), (x2, y2), abs((x1 - x2 + 1) * (y1 - y2 + 1)))
# print(max(p1), max(p2))

print(f"p1: {max(p1)}")
print(f"p2: {max(p2)}")
