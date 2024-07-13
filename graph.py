graph = {}
num_nodes = int(input("Enter number of nodes: "))
for _ in range(num_nodes):
    node = input("Enter node: ")
    adj_nodes = input(f"Enter adjacent nodes for {node} (space-separated): ").split()
    graph[node] = adj_nodes

while True:
    node = input("Enter node to find adjacent nodes (or 'exit' to quit): ")
    if node == 'exit':
        break
    print(f"Adjacent nodes of {node}: {', '.join(graph.get(node, []))}")                       
