graph = {}
total_paths = 0

# parse input into an adjacency list representation of the graph
with open("day11_input.txt", "r") as f:
    for line in f:
        node = line[:3]
        neighbours = line[4:].strip().split()
        graph[node] = neighbours

# initialise bfs queue with 'you' as starter node
queue = [(node, {'you'}) for node in graph['you']]

# perform bfs on whole graph, counting each path that ends at 'out'
while len(queue) > 0:
    curr = queue.pop(0)
    curr_node = curr[0]
    visited = curr[1].copy()
    for next_node in graph[curr_node]:
        if next_node == 'out':
            total_paths += 1
        elif next_node not in visited:
            visited.add(curr_node)
            queue.append((next_node, visited))

# print result
print(total_paths)