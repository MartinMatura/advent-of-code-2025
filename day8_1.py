import math

coords = []
circuits = []
circuit_mappings = {} # keep track of which position is in which circuit without needing to search circuits

# parse input into list of coordinates
with open("day8_input.txt", "r") as f:
    for line in f:
        coords.append(tuple(map(int, line.strip().split(','))))

# helper function to calculate distance between two positions
def dist(l1, l2):
    dist = 0
    for i in range(len(l1)):
        dist += (l1[i] - l2[i])**2
    return math.sqrt(dist)

# get list of all pairings of positions and sort it by distance between the positions
pairings = [[pos1, pos2] for i, pos1 in enumerate(coords) for pos2 in coords[i+1:]]
pairings.sort(key=lambda x: dist(x[0], x[1]))

# perform the first 1000 connections
for i in range(1000):
    closest_pair = pairings.pop(0)
    if closest_pair[0] not in circuit_mappings.keys() and closest_pair[1] not in circuit_mappings.keys():
        # neither position is in a circuit yet -> create a new one for them
        circuits.append(closest_pair)
        circuit_mappings[closest_pair[0]] = len(circuits) - 1
        circuit_mappings[closest_pair[1]] = len(circuits) - 1
    elif closest_pair[0] in circuit_mappings.keys() and closest_pair[1] not in circuit_mappings.keys():
        # first position is in a circuit and second one isn't -> add second position to first's circuit
        circuit = circuit_mappings[closest_pair[0]]
        circuits[circuit].append(closest_pair[1])
        circuit_mappings[closest_pair[1]] = circuit
    elif closest_pair[0] not in circuit_mappings.keys() and closest_pair[1] in circuit_mappings.keys():
        # second position is in a circuit and first one isn't -> add first position to to second's circuit
        circuit = circuit_mappings[closest_pair[1]]
        circuits[circuit].append(closest_pair[0])
        circuit_mappings[closest_pair[0]] = circuit
    elif circuit_mappings[closest_pair[0]] != circuit_mappings[closest_pair[1]]:
        # both positions are in a circuit but not the same one -> merge the circuits into the one with a lower index
        circuit1 = circuit_mappings[closest_pair[0]]
        circuit2 = circuit_mappings[closest_pair[1]]
        if circuit2 < circuit1: # ensure that we merge into circuit with lower index and don't create gaps in list
            circuit1, circuit2 = circuit2, circuit1 
        # merge into first circuit
        for pos in circuits[circuit2]:
            circuits[circuit1].append(pos)
            circuit_mappings[pos] = circuit1
        circuits.pop(circuit2) # remove second circuit
        # adjust circuit mappings to reflect removed circuit
        for moved_circuit in circuits[circuit2:]:
            for pos in moved_circuit:
                circuit_mappings[pos] -= 1

# calculate result
circuit_lengths = sorted([len(circuit) for circuit in circuits])
print(circuit_lengths[-1] * circuit_lengths[-2] * circuit_lengths[-3])