_input = list(map(list, open("input.txt").read().splitlines()))
neighbors = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0)]
counts = dict()
x_lim, y_lim = len(_input[0]), len(_input)
for y in range(y_lim):
    for x in range(x_lim):
        if _input[y][x] == "@":
            counts[(x, y)] = 0
            for i, j in neighbors:
                if 0 <= x+i < x_lim and 0 <= y+j < y_lim:
                    counts[(x, y)] += "@" == _input[y+j][x+i]
print(len([c for c in counts.values() if c < 4]))
