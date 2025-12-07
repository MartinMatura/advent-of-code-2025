beams = [0 for _ in range(141)] # initialise list to count number of beams collected in each column
timeline_count = 1
with open("day7_input.txt", "r") as f:
    beams[(f.readline().find("S"))] += 1 # initialise source beam
    even_line = False
    # at each line add number of beams hitting each splitter to neighbouring columns
    for line in f:
        even_line = not even_line 
        if not even_line:
            splitters = set()
            for i, char in enumerate(line):
                if char == '^':
                    beams[i-1] += beams[i]
                    beams[i+1] += beams[i]
                    beams[i] = 0

# get total number of timelines by summing number of beams reaching final row
print(sum(beams))