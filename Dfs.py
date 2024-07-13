def dfs(graph, start):
    visited = set()  
    def dfs_code(node):
        visited.add(node)
        print(f"Node: {node}")
        print(f"  Edges: {graph[node]}")
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_code(neighbor)
    dfs_code(start)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start_node = 'A'
dfs(graph, start_node)

