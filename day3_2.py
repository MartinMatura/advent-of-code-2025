max_joltage = 0
with open("day3_input.txt", "r") as f:
    for bank in f:
        bank = bank.strip()
        largest = list(map(int, bank[len(bank)-12:])) # start with 12 rightmost values as largest
        for battery in reversed(bank[:-12]): # move over remaining values from right to left
            joltage = int(battery)
            insert_idx = -1
            remove_idx = -1
            for i in range(12): # we want to insert in a new number in the first position where the current number is lower
                if largest[i] < joltage: # if such a position is found
                    insert_idx = i # store index where we want to insert new value
                    remove_idx = 11 # if no better place is found by for-loop below, remove the last number from largest
                    for j in range(11): # we want to remove the first number in largest that is lower than its successor to make space for the new number
                        if largest[j] < largest[j+1]: # if such a position is found (if no is found, last number will be removed)
                            remove_idx = j # store it in remove_idx
                            break # we only care about first position that satisfies this so now we can break the loop
                    break # again, only care about first position that satisfies the condition
                elif largest[i] > joltage: # stop looking if we find a position where the number is greater than the new number
                    break
            if insert_idx > -1 and remove_idx > -1: # if positions to insert and remove were found:
                largest.insert(insert_idx, joltage) # insert new number
                largest.pop(remove_idx + 1) # remove_idx incremented by 1 to account for new number being inserted before it
        max_joltage += int("".join(map(str, largest))) # convert list of numbers to int
print(max_joltage)