import math

rows = open("input.txt").read().split("\n")
boxes = [tuple(int(c) for c in x.split(",") if c) for x in rows]

distances = {}
for box in boxes:
    x, y, z = box
    for box2 in boxes:
        if box == box2:
            continue
        x2, y2, z2 = box2
        xd, yd, zd = (x - x2) ** 2, (y - y2) ** 2, (z - z2) ** 2
        distance = math.sqrt(xd + yd + zd)
        if (box, box2) not in distances and (box2, box) not in distances:
            distances[(box, box2)] = distance

circuits = {i: [box] for i, box in enumerate(boxes)}
wires = 0
for dist in sorted(
    distances.items(),
    key=lambda x: x[1],
):
    if wires == 1000:
        p1 = math.prod(sorted([len(c) for k, c in circuits.items()], reverse=True)[:3])
        print(f"p1: {p1}")
    box1, box2 = dist[0]
    box1_circ, box2_circ = None, None
    for circ_id, circ in circuits.items():
        if box1 in circ:
            box1_circ = circ_id
        if box2 in circ:
            box2_circ = circ_id
    if box2_circ != box1_circ:
        circuits[box2_circ] = circuits[box2_circ] + circuits[box1_circ]
        del circuits[box1_circ]
        if len(circuits) == 1:
            print(f"p2: {box1[0] * box2[0]}")
            break
    wires += 1
