from math import ceil
_input = open("input.txt").read().split(',')

p1, p2 = 0, 0
for id_range in _input:
    beg, end = map(int, id_range.split("-"))
    for id in range(beg, end+1):
        p2_break = False
        if str(id)[len(str(id))//2:] == str(id)[:len(str(id))//2]:
            p1 += id
        for i in range(1, ceil(len(str(id))/2)+2):
            chunks = []
            for k in range(0, len(str(id))+1, i):
                if str(id)[k:k+i]:
                    chunks.append(str(id)[k:k+i])
            if len(set(chunks)) == 1 and len(chunks) != 1:
                p2 += int(id)
                break
print(p1, p2)
