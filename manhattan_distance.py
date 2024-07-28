graph = {
  'A': (2, 4),
  'B': (5, 1),
  'C': (6, 3)
}
def manhattan_distance(n1, n2):
  x1, y1 = n1
  x2, y2 = n2
  distance = abs(x1 - x2) + abs(y1 - y2)
  return distance
def calculate_distances(graph):
  for node1, parallel1 in graph.items():
    for node2, parallel2 in graph.items():
      if node1 != node2:
        distance = manhattan_distance(parallel1, parallel2)
        print(f"Distance between {node1} and {node2}: {distance}")
calculate_distances(graph)
