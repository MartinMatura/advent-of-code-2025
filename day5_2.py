ranges = []
fresh_ids = 0

# parse input into list of ranges of fresh ingredient ids, ignore actual ids below
with open("day5_input.txt", "r") as f:
    for line in f.readlines():
        if line.strip() == '':
            break
        new_range = list(map(int, line.strip().split("-")))
        ranges.append(new_range)

# sort ranges by starting value to remove need for checking backwards or backtracking when merging ranges
ranges.sort(key=lambda x: x[0])

# merge overlapping ranges together
i = 0
while i < len(ranges)-1:
    curr_range = ranges[i]
    next_range = ranges[i+1]
    # if next range starts within current range, merge it with current range
    if next_range[0] <= curr_range[1]:
        ranges[i][1] = max(next_range[1], curr_range[1])
        ranges.pop(i+1)
    else: # no range overlaps with current range so move to next
        i += 1

# count total number of ids in merged ranges
for range_start, range_end in ranges:
    fresh_ids += range_end - range_start + 1

print(fresh_ids)