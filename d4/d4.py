_input = list(map(list, open("input.txt").read().splitlines()))
neighbors = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0)]
x_lim, y_lim, removed = len(_input[0]), len(_input), []

def removable():
    counts = dict()
    for y in range(y_lim):
        for x in range(x_lim):
            if _input[y][x] == "@":
                counts[(x, y)] = 0
                for i, j in neighbors:
                    if 0 <= x+i < x_lim and 0 <= y+j < y_lim:
                        counts[(x, y)] += "@" == _input[y+j][x+i]
    remove = {k:v for k, v in counts.items() if v < 4}
    return remove

def remove(coords):
    for x, y in coords:
        _input[y][x] = "x"
    removed.append(len(coords))

while paper := removable():
    remove(paper.keys())

print(f"p1: {removed[0]}, p2: {sum(removed)}")
