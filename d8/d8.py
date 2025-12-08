import math
from itertools import combinations

boxes = [tuple(map(int, line.split(","))) for line in open("input.txt") if line.strip()]
distances = {(a, b): math.dist(a, b) for a, b in combinations(boxes, 2)}
circuits = {i: [box] for i, box in enumerate(boxes)}

for i, dist in enumerate(
    sorted(
        distances.items(),
        key=lambda x: x[1],
    )
):
    if i == 1000:
        p1 = math.prod(sorted([len(c) for k, c in circuits.items()], reverse=True)[:3])
        print(f"p1: {p1}")
    box1, box2 = dist[0]
    box1_circ = next(cid for cid, circ in circuits.items() if box1 in circ)
    box2_circ = next(cid for cid, circ in circuits.items() if box2 in circ)
    if box2_circ != box1_circ:
        circuits[box2_circ] = circuits[box2_circ] + circuits[box1_circ]
        del circuits[box1_circ]
        if len(circuits) == 1:
            print(f"p2: {box1[0] * box2[0]}")
            break
