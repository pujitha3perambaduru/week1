def a_star(graph, start, goal, heuristic):
    frontnode = [(0 + heuristic[start], 0, start)]
    openset = {}
    closeset = {}
    openset[start] = None
    closeset[start] = 0
    while frontnode:
        frontnode.sort()
        cost,current_cost, current_node = frontnode.pop(0)
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = openset[current_node]
            path.reverse()
            return path
        for neighbor, weight in graph[current_node]:
            new_cost = current_cost + weight
            if neighbor not in closeset or new_cost < closeset[neighbor]:
                closeset[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                frontnode.append((priority, new_cost, neighbor))
                openset[neighbor] = current_node
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
path = a_star(graph, start_node, goal_node, heuristic)

print("Path found:", path)

