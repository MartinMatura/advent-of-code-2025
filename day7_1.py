beam_cols = set() # store columns in input where a beam currently is
split_count = 0
with open("day7_input.txt", "r") as f:
    beam_cols.add(f.readline().find("S"))
    even_line = False # only even lines contain splitters
    # for each line, split any beam that hits a splitter, increment split_count
    # accordingly and update beam_cols
    for line in f:
        even_line = not even_line 
        if not even_line:
            new_beam_cols = set([col for col in beam_cols]) # make a copy of beam_cols to update as we iterate over original
            # check if each beam hits a splitter and split it if it does
            for col in beam_cols:
                if line[col] == '^':
                    split_count += 1
                    new_beam_cols.remove(col)
                    new_beam_cols.add(col+1)
                    new_beam_cols.add(col-1)
            beam_cols = new_beam_cols # update beam_cols

print(split_count)