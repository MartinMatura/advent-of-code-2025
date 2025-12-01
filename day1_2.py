position = 50
n_zeros = 0
with open("day1_input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        clicks = int(line[1:])
        n_zeros += clicks//100 # count number of full rotations of dial
        clicks %= 100 # get number of clicks after full rotations
        if line[0] == "L":
            if position == 0: # cover edge case where 0 would get counted twice if rotation left started from 0
                n_zeros -= 1
            position -= clicks # calculate dial position
            if position < 0: # count case when dial crosses 0 during rotation
                n_zeros += 1
                position += 100 # normalise dial position to correct range
            elif position == 0: # count case when dial ends at 0 after rotation
                n_zeros += 1
        else:
            position += clicks # calculate dial position
            if position > 99: # count case when dial crosses 0 during rotation
                n_zeros += 1
                position -= 100 # normalise dial position to correct range
print(n_zeros)