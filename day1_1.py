position = 50
n_zeros = 0
with open("day1_input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line[0] == "L":
            position = (position - int(line[1:]))%100
        else:
            position = (position + int(line[1:]))%100
        if position == 0:
            n_zeros += 1
print(n_zeros)