import math
def euclidean_distance(path1, path2):
  x1, y1 = path1
  x2, y2 = path2
  dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
  return dist
def calculate_distances(nodes):
  for node1, pos1 in nodes.items():
    for node2, pos2 in nodes.items():
      if node1 != node2:
        dist = euclidean_distance(pos1, pos2)
        print(f"Distance between {node1} and {node2}: {dist:.2f}")
nodes = {
          'A': (2, 4), 
          'B': (5, 1), 
          'C': (2, 3)
         }
calculate_distances(nodes)




