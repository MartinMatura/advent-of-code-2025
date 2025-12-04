rows = []
# parse input into matrix of individual chars
with open("day4_input.txt", "r") as f:
    for line in f:
        rows.append(list(line.strip()))

accessible_rolls = 0
neighbours = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)] # coordinate increments of all neighbour cells relative to a given cell

for row in range(len(rows)):
    for col in range(len(rows[0])):
        if rows[row][col] == '@':
            adj_rolls = 0
            # if they are in valid range, check each neighbouring set of coords whether they contain a roll
            for neighbour in neighbours:
                neighbour_row = row+neighbour[0]
                neighbour_col = col+neighbour[1]
                if neighbour_row < (len(rows)) and neighbour_row >= 0 and neighbour_col < (len(rows[0])) and neighbour_col >= 0 and rows[neighbour_row][neighbour_col] == '@':
                    adj_rolls += 1
            # if current roll neighbours less than 4 rolls, count it as accessible
            if adj_rolls < 4:
                accessible_rolls += 1

print(accessible_rolls)
        
