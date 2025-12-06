_input = map(list, open("input.txt").read().splitlines())

joltz = 0
for row in _input:
    #print(row)
    max_left, max_right = 0, 1
    for i in range(len(row)):
        if i < len(row)-1:
            if int(row[i]) > int(row[max_left]) or i == max_left:
                max_left = i
                max_right = i + 1
                continue
        if int(row[i]) > int(row[max_right]):
            max_right = i
    joltz += int(row[max_left] + row[max_right])
    #print(f"{row[max_left]}{row[max_right]}")

print(joltz)