coords = set()

#parse input into set of coords
with open("day9_input.txt", "r") as f:
    for line in f:
        coords.add(tuple(map(int, line.strip().split(','))))

# helper function to calculate area between 2 coords
def area(l1, l2):
    return (abs(l1[0]-l2[0])+1)*(abs(l1[1]-l2[1])+1)

# store current furthest pair and its area
furthest_pair = []
max_area = 0

# iterate over all coords to find pair with largest area
for pos1 in coords:
    for pos2 in coords:
        new_area = area(pos1, pos2) 
        if new_area > max_area:
            furthest_pair = [pos1, pos2]
            max_area = new_area

# print result
print(area(furthest_pair[0], furthest_pair[1]))