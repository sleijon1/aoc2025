from itertools import combinations

from tqdm import tqdm

tiles = [tuple(map(int, r.split(","))) for r in open("input.txt").read().split("\n")]

green_tiles = set()
red_corners = set()
for (x1, y1), (x2, y2) in combinations(tiles, 2):
    if x1 == x2:
        red_corners.add((x1, y1))
        red_corners.add((x1, y2))
        for y in range(min(y1, y2), max(y1, y2) + 1):
            green_tiles.add((x1, y))
    elif y1 == y2:
        red_corners.add((x1, y1))
        red_corners.add((x2, y1))
        for x in range(min(x1, x2), max(x1, x2) + 1):
            green_tiles.add((x, y1))

green_tiles = tuple(green_tiles)

p1sol, p2sol = [], []


from functools import lru_cache

doomed_tiles = set()
print(len(green_tiles))
print(len(red_corners))


@lru_cache
def rect_edges_fully_covered(bottom_edge, top_edge, left_edge, right_edge):
    edge_points = bottom_edge + top_edge + left_edge + right_edge
    if any([ep in doomed_tiles for ep in edge_points]):
        return False
    for x, y in edge_points:
        left, right, up, down, on_top = False, False, False, False, False
        for tx, ty in red_corners:
            if ty == y:
                if tx > x:
                    right = True
                elif tx < x:
                    left = True
                elif tx == x:
                    on_top = True
            if tx == x:
                if ty < y:
                    up = True
                elif ty > y:
                    down = True
                elif ty == y:
                    on_top = True
            if sum([left, right, on_top]) >= 2 or sum([up, down, on_top]) >= 2:
                break

        if not (sum([left, right, on_top]) >= 2 or sum([up, down, on_top]) >= 2):
            doomed_tiles.add(edge_points)
            return False  # one point fails → rectangle not fully covered
    return True  # all points passed


N = len(tiles)
iterations = N * (N - 1) / 2
for (x1, y1), (x2, y2) in tqdm(combinations(tiles, 2), total=iterations):
    p1sol.append(abs((x1 - x2 + 1) * (y1 - y2 + 1)))
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
    if rect_edges_fully_covered(bottom_edge, top_edge, left_edge, right_edge):
        p2sol.append(abs((x1 - x2 + 1) * (y1 - y2 + 1)))

print(f"p1: {max(p1sol)}")
print(f"p2: {max(p2sol)}")
