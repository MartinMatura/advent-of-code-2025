rows = []
# parse input into matrix of individual chars
with open("day4_input.txt", "r") as f:
    for line in f:
        rows.append(list(line.strip()))

removable_rolls = 0
neighbours = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)] # coordinate increments of all neighbour cells relative to a given cell
queue = [] # queue of coordinates that contain a roll and need to be checked for removability
coords_in_queue = set() # set to keep track of all entries currently in queue to check coordinates aren't being added more times
                        # -> checking presence in a set is computationally faster than in a list

# initialise queue with all sets of coordinates that contain a roll 
for row in range(len(rows)):
    for col in range(len(rows[0])):
        if rows[row][col] == '@':
            queue.append((row, col))
            coords_in_queue.add((row, col))
            adj_rolls = 0
            
# while queue is not empty, pop elements one at a time and check their removability
# -> if a roll is removable (neighbours less than 4 rolls), remove it and add all its neighbour rolls to the queue
while len(queue) > 0:
    row, col = queue.pop(0)
    coords_in_queue.remove((row, col))
    adj_rolls = []
    # check removability
    for neighbour in neighbours:
        neighbour_row = row+neighbour[0]
        neighbour_col = col+neighbour[1]
        if neighbour_row < (len(rows)) and neighbour_row >= 0 and neighbour_col < (len(rows[0])) and neighbour_col >= 0 and rows[neighbour_row][neighbour_col] == '@':
            adj_rolls.append((neighbour_row, neighbour_col))
    # if removable, add adjacent rolls to the queue (if they aren't already there) and remove the roll
    if len(adj_rolls) < 4:
        removable_rolls += 1
        for adj_roll in adj_rolls:
            if adj_roll not in coords_in_queue:
                queue.append(adj_roll)
                coords_in_queue.add(adj_roll)
        rows[row][col] = '.'

print(removable_rolls)
        