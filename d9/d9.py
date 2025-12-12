from itertools import combinations

from tqdm import tqdm

tiles = [tuple(map(int, r.split(","))) for r in open("input.txt").read().split("\n")]

green_tiles = set()
for (x1, y1), (x2, y2) in combinations(tiles, 2):
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            green_tiles.add((x1, y))
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            green_tiles.add((x, y1))


p1sol, p2sol = [], []


def rect_edges_fully_covered(bottom_edge, top_edge, left_edge, right_edge, green_tiles):
    """
    Check if all points on the rectangle edges have both a green tile to the left and to the right.
    green_tiles: set of (x, y) points
    """
    # Combine all edge points
    edge_points = bottom_edge + top_edge + left_edge + right_edge

    for x, y in edge_points:
        # Check left
        left_exists = any((xi, y) in green_tiles for xi in range(x_min, x))
        # Check right
        right_exists = any((xi, y) in green_tiles for xi in range(x + 1, x_max + 1))
        if not (left_exists and right_exists):
            return False  # one point fails → rectangle not fully covered
    return True  # all points passed


N = len(tiles)
iterations = N * (N - 1) / 2
for (x1, y1), (x2, y2) in tqdm(combinations(tiles, 2), total=iterations):
    p1sol.append(abs((x1 - x2 + 1) * (y1 - y2 + 1)))
    # Rectangle bounds
    x_min, y_min, x_max, y_max = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)

    # Horizontal edges (points)
    bottom_edge = [(x, y_min) for x in range(x_min, x_max + 1)]
    top_edge = [(x, y_max) for x in range(x_min, x_max + 1)]

    # Vertical edges (points), exclude corners to avoid duplicates
    left_edge = [(x_min, y) for y in range(y_min + 1, y_max)]
    right_edge = [(x_max, y) for y in range(y_min + 1, y_max)]

    # outside = False
    # for p1, p2 in green_lines:
    #    if line_intersects_rect_edges(p1, p2, rect):
    #        outside = True
    #        break
    if rect_edges_fully_covered(
        bottom_edge, top_edge, left_edge, right_edge, green_tiles
    ):
        p2sol.append(abs((x1 - x2 + 1) * (y1 - y2 + 1)))

print(f"p1: {max(p1sol)}")
print(f"p2: {max(p2sol)}")
