_input = list(map(list, open("input.txt").read().splitlines()))

def epic_j(b):
    j = 0
    for row in _input:
        indices = [0]
        conc = ""
        for i in range(b, 0, -1):
            idx, val = max(enumerate(row[indices[-1]:len(row)-i+1]), key=lambda x: x[1])
            indices.append(indices[-1]+ idx + 1)
            conc += val
        j += int(conc)
    return j

print(f"p1: {epic_j(2)}, p2: {epic_j(12)}")