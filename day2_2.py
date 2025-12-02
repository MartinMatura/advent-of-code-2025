def check_invalid(id):
    id = str(id) # cast id to string for slicing and comparison
    whole_divisors = [] 
    # get list of whole divisors of len(id) 
    # -> gives number of equal-size slices that id can be split into 
    for i in range(2, len(id)+1):
        if len(id)%i==0:
            whole_divisors.append(i)
    # for each divisor check if all slices of given size are the same
    for d in whole_divisors:
        unique_sequences = set([id[(i*len(id))//d:((i+1)*len(id))//d] for i in range(d)]) # uniqueness checked by casting list of all slices to a set
        if len(unique_sequences) == 1:
            return True
    return False

id_ranges = []
with open("day2_input.txt", "r") as f:
    id_ranges = f.readline().strip().split(",") # parse id ranges
invalid_sum = 0
for id_range in id_ranges:
    start, end = map(int, id_range.split("-")) # parse id ranges into ints
    for id in range(start, end+1):
        if check_invalid(id):
            invalid_sum += id
print(invalid_sum)
