_dir = {"L": -1, "R": 1}
state, p1, p2 = 50, 0, 0
for line in open("input.txt").read().split("\n"):
    if state == 0:
        p1 += 1
    for _ in range(int(line[1:])):
        if state == 0 and line[0] == "L":
            state = 99
        elif state == 99 and line[0] == "R":
            state = 0
        else:
            state += _dir[line[0]]
        if state == 0:
            p2 += 1
    
print(f"p1: {p1}, p2: {p2}")