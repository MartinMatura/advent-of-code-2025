id_ranges = []
with open("day2_input.txt", "r") as f:
    id_ranges = f.readline().strip().split(",") # parse id ranges
invalid_sum = 0
for id_range in id_ranges:
    start, end = map(int, id_range.split("-")) # parse id range into ints
    for i in range(start, end+1):
        str_i = str(i) # cast id to string for slicing and comparison
        if str_i[:len(str_i)//2] == str_i[len(str_i)//2:]: # check if both halfs of id string are same
            invalid_sum += i
print(invalid_sum)