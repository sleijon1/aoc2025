from itertools import combinations

tiles = [tuple(map(int, l.split(","))) for l in open("input.txt")]

edges = list(zip(tiles, tiles[1:] + tiles[:1]))

V, H = [], []
for (x1, y1), (x2, y2) in edges:
    if x1 == x2:
        V.append((x1, min(y1, y2), max(y1, y2)))
    else:
        H.append((y1, min(x1, x2), max(x1, x2)))


def inside(px, py):
    # raycasting
    return sum(x > px and y1 <= py < y2 for x, y1, y2 in V) % 2


def cuts(x0, y0, x1, y1):
    # green line intersecting rect
    # starting point furthest to the right max(y1_, y0)
    # ending point furthest to the left    min(y2_, y1)
    return any(
        (x0 < x < x1 and max(y1_, y0) < min(y2_, y1)) for x, y1_, y2_ in V
    ) or any((y0 < y < y1 and max(x1_, x0) < min(x2_, x1)) for y, x1_, x2_ in H)


def valid(a, b):
    x0, x1 = sorted((a[0], b[0]))
    y0, y1 = sorted((a[1], b[1]))
    return inside(x0 + 1, y0 + 1) and not cuts(x0, y0, x1, y1)


# A rectangle is invalid if:
# 1) a polygon edge cuts through its interior (partial overlap)
# 2) it lies completely outside the polygon
#
# If no edge cuts it, testing one interior point via raycasting
# is sufficient to determine inside vs outside.
best = max(
    (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    for (x1, y1), (x2, y2) in combinations(tiles, 2)
    if valid((x1, y1), (x2, y2))
)

print(best)
