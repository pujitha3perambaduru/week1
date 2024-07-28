 def bestfs(graph, start, goal, heuristic):
    firstnode = [(heuristic[start], start)]
    tracknode = {}
    tracknode[start] = None
    while firstnode:
        firstnode.sort()
        current_priority, current_node = firstnode.pop(0)
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = tracknode[current_node]
            path.reverse()
            return path
        for neighbor, cost in graph[current_node]:
            if neighbor not in tracknode:  # If neighbor hasn't been explored yet
                priority = heuristic[neighbor]
                firstnode.append((priority, neighbor))
                tracknode[neighbor] = current_node
    return None 
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 5), ('E', 1)],
    'C': [('F', 2)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}
heuristic = {
    'A': 6,
    'B': 5,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 1,
    'G': 0
}
start_node = 'A'
goal_node = 'G'
path = bestfs(graph, start_node, goal_node, heuristic)
print("Path found:", path)

