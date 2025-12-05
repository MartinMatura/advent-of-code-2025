ranges = []
ids = []
input_is_range = True 
fresh_ingredients = 0

# parse input into list of ranges of fresh ingredient ids and list of actual ids
with open("day5_input.txt", "r") as f:
    for line in f.readlines():
        if line.strip() == '':
            input_is_range = False
            continue
        if input_is_range:
            ranges.append(list(map(int, line.strip().split("-"))))
        else:
            ids.append(int(line.strip()))

# count how many ids fall into one of the ranges
for id in ids:
    for range_start, range_end in ranges:
        if id >= range_start and id <= range_end:
            fresh_ingredients += 1
            break

print(fresh_ingredients)

