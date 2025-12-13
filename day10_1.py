machines = []
total_presses = 0

# parse input into list of machines (represented as dicts)
with open("day10_input.txt", "r") as f:
    for line in f:
        lights_str = line[1:line.find(']')]
        lights = [True if char == '#' else False for char in lights_str]
        buttons_str = line[line.find(']')+1:line.find('{')-1].split()
        buttons = []
        for button in buttons_str:
            button = tuple(map(int, button.strip('()').split(',')))
            buttons.append(button)
        joltages = tuple(map(int, line[line.find('{')+1:-2].split(',')))
        machines.append({'lights': lights, 'buttons': buttons, 'joltages': joltages})

# helper function to apply button press to current state of indicator lights
def apply_button(state, button):
    state_copy = state[:]
    for i in button:
        state_copy[i] = not state[i]
    return state_copy

# find min number of button presses needed to get to target state for each machine
for machine in machines:
    target = machine['lights']
    # initialise queue of states with initial state of all lights off and 0 buttons pressed so far
    state_queue = [([False for _ in range(len(machine['lights']))], 0)]
    # track states which were already seen that will not get added to the queue again
    seen = {(tuple(tuple(state_queue[0][0])))}
    found = False # condition to exit the loop below
    # while target state isn't reached, pop a state from queue, apply all buttons to it
    # and add all resulting states that weren't seen yet back into the queue
    while not found:
        curr_state = state_queue.pop(0)
        presses_made = curr_state[1]
        for button in machine['buttons']:
            new_state = apply_button(curr_state[0][:], button)
            if new_state == target:
                total_presses += presses_made + 1
                found = True
                break
            elif tuple(new_state) not in seen:
                state_queue.append((new_state, presses_made+1))
                seen.add(tuple(new_state))

# print result
print(total_presses)