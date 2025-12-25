from functools import lru_cache

connections = {}
with open("input.txt") as f:
    for line in f:
        src, dsts = line.strip().split(": ")
        connections[src] = dsts.split()


@lru_cache(maxsize=None)
def count_paths(src: str, target: str) -> int:
    if src == target:
        return 1
    total = 0
    for nxt in connections.get(src, []):
        total += count_paths(nxt, target)
    return total


start = "svr"
a = "dac"
b = "fft"
end = "out"

# 1) svr -> dac -> fft -> out
seg1 = count_paths(start, a) * count_paths(a, b) * count_paths(b, end)

# 2) svr -> fft -> dac -> out
seg2 = count_paths(start, b) * count_paths(b, a) * count_paths(a, end)

print(seg1 + seg2)


# For each order of paths from start node to end node
# sum up the number of paths between each sub path - paths(A→C via B) = paths(A→B) × paths(B→C)
# conditions:
# - none of the subpaths contains cycles (implicit in number of paths being finite) and so none of the complete paths contain cycles
