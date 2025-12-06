# parse input into list of lists of numbers of each line and list of operations on last line
lines = []
operations = []
with open("day6_input.txt", "r") as f:
    for i in range(4):
        lines.append(list(map(int, f.readline().strip().split())))
    operations = f.readline().strip().split()

# perform appropriate operation for each set of numbers and add result to total
total = 0
for i, op, in enumerate(operations):
    nums = [lines[j][i] for j in range(len(lines))]
    if op == '+':
        total += sum(nums)
    elif op == '*':
        prod = 1
        for num in nums:
            prod *= num
        total += prod

print(total)


        