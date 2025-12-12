from concurrent.futures import ProcessPoolExecutor, as_completed
from functools import lru_cache
from itertools import combinations

from tqdm import tqdm

tiles = [tuple(map(int, r.split(","))) for r in open("input.txt").read().split("\n")]

green_tiles = set()
allowed_tiles = set()
for (x1, y1), (x2, y2) in combinations(tiles, 2):
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            green_tiles.add((x1, y))
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            green_tiles.add((x, y1))

green_tiles = tuple(green_tiles)

x_ranges = dict()
for x, y in tqdm(green_tiles):
    if y in x_ranges:
        mix, maxx = x_ranges[y]
        if x < mix:
            mix = x
        if x > maxx:
            maxx = x
        x_ranges[y] = (mix, maxx)
    else:
        x_ranges[y] = (x, x)


p1sol, p2sol = [], []


@lru_cache
def rect_edges_fully_covered2(bottom_edge, top_edge, left_edge, right_edge):
    edge_points = bottom_edge + top_edge + left_edge + right_edge
    for x, y in edge_points:
        try:
            mix, max = x_ranges[y]
            if not mix <= x <= max:
                return False
        except KeyError:
            return False

    return True


N = len(tiles)
iterations = N * (N - 1) / 2


def rectangles(comb):
    (x1, y1), (x2, y2) = comb
    # p2sol = []
    # for (x1, y1), (x2, y2) in combinations:
    #   p1sol.append(abs((x1 - x2 + 1) * (y1 - y2 + 1)))
    # Rectangle bounds
    x_min, y_min, x_max, y_max = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)

    # Horizontal edges (points)
    bottom_edge = tuple((x, y_min) for x in range(x_min, x_max + 1))
    top_edge = tuple((x, y_max) for x in range(x_min, x_max + 1))

    # Vertical edges (points), exclude corners to avoid duplicates
    left_edge = tuple((x_min, y) for y in range(y_min, y_max + 1))
    right_edge = tuple((x_max, y) for y in range(y_min, y_max + 1))

    # outside = False
    # for p1, p2 in green_lines:
    #    if line_intersects_rect_edges(p1, p2, rect):
    #        outside = True
    #        break
    if rect_edges_fully_covered2(bottom_edge, top_edge, left_edge, right_edge):
        return abs((x1 - x2 + 1) * (y1 - y2 + 1))
        p2sol.append(abs((x1 - x2 + 1) * (y1 - y2 + 1)))
    return 0


work = combinations(tiles, 2)
with ProcessPoolExecutor() as exe:
    futures = [exe.submit(rectangles, combo) for combo in work]

results = []
for f in tqdm(as_completed(futures), total=len(futures)):
    results.append(f.result())
# print(results)
# sprint(f"p1: {max(p1sol)}")
print(f"p2: {max(results)}")
