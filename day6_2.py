# read file
with open("day6_input.txt", "r") as f:
    file = f.read()

# find length of line in input and initialise pointers to the start of each line
n_of_lines = 5
line_length = file.find("\n")
pointers = [i*(line_length+1) for i in range(n_of_lines)]
total = 0

# move left to right through file, at each step finding all the numbers in the current
# "group", performing the appropriate operation, adding the result to the total and moving 
# the pointers to the start of the next "group"
while pointers[0] < line_length:
    # find how many columns the current group spans over
    column_ends = [min(file.find(" ", pointer), file.find("\n", pointer))  for pointer in pointers[:-1]]
    max_column_len = max([column_end - pointer for column_end, pointer in zip(column_ends, pointers[:-1])])
    # read all numbers in all columns of the group from (moving left to right) and store them in nums
    nums = []
    for i in range(max_column_len):
        num = 0
        order = 0
        # read individual integers from bottom to top, ignoring any leading or trailing whitespace
        for pointer in reversed(pointers[:-1]):
            char = file[pointer+i]
            if char != " ":
                num += int(char) * 10**order
                order += 1
        nums.append(num)
    # find the operation associated with this group
    operation = file[pointers[-1]]
    # perform the operation and add the result to the total
    if operation == '+':
        total += sum(nums)
    elif operation == '*':
        prod = 1
        for num in nums:
            prod *= num
        total += prod
    # move all pointers past this group to the start of the next group
    for i in range(len(pointers)):
        pointers[i] += max_column_len + 1
        
print(total)