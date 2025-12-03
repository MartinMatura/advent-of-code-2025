max_joltage = 0
with open("day3_input.txt", "r") as f:
    for bank in f:
        bank = bank.strip()
        largest = [int(bank[0]), int(bank[1])] # start with first two values as largest
        for battery in bank[2:]: # iterate over all other joltage values in given bank
            joltage = int(battery)
            if largest[1] > largest[0]: # if second number in largest is ever larger than the first
                largest[0] = largest[1] # move second number to first position
                largest[1] = joltage # replace number in second position with new number
            elif joltage > largest[1]: # if new number is larger than number in second position
                largest[1] = joltage # replace number in second position with new number
        max_joltage += 10*largest[0] + largest[1]
print(max_joltage)
