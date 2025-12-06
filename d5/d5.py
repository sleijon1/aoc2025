ranges, ids = open("input.txt").read().split("\n\n")
ids = list(map(int, ids.split("\n")))
ranges = [(int(r.split("-")[0]), int(r.split("-")[1])+1) for r in ranges.split("\n")]
fresh = []
for id in ids:
    for (b, e) in ranges:
        if id in range(b, e):
            fresh.append(id)
            break

def unique_ranges(ranges):
    non_overlapping = [(0, 0)]
    for b1, e1 in ranges:
        overlap = False
        for i, (b2, e2) in enumerate(non_overlapping):
            if b1 <= e2 and e1 >= b2:
                non_overlapping[i] = (min(b1, b2), max(e1, e2))
                overlap = True
        if not overlap:
            non_overlapping.append((b1, e1))
    return non_overlapping

for _ in range(2):
    ranges = unique_ranges(ranges)
    
p2 = sum([e-b for b, e in ranges])
print(f"p1: {len(fresh)} p2: {p2}")
