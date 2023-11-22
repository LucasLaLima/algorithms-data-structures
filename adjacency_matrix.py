"""
1. Create kxk matrix
2. Row and column represent the nodes of the graph
3. If edge exists between nodes u & v, value at matrix intersection is 1, otherwise 0

3 Types of matricies:
1) Non-directional matrix (symmmetric across matrix main diagona (top-left to bottom-right)
2) Directional matrix
3) Weighted matrix (Values are weight sizes instead of 1)

Complexity:
- Run time to check edge: 0(1)
- Space time complexity: O(v^2)
where v is the number of nodes
"""

import numpy as np
import pandas as pd

# Graph Class
class Graph:
  def __init__(self, size):
    self.size = (size, size)
    self.matrix = np.zeros((size, size))
    self.nodes = []
    return

  def addNode(self, node):
    self.nodes.append(node.data)
    return

  def addEdge(self, src, dst):
    #src is row, dst is column
    self.matrix[src][dst] = 1
    return
    
  def checkEdge(self, src, dst):
    if self.matrix[src][dst]==1:
      return True
    else:
      return False

  def __str__(self):
    row_labels = self.nodes
    column_labels = self.nodes
    df = pd.DataFrame(self.matrix, index=row_labels, columns=column_labels)
    return df.to_string()

# Node Class
class Node:
  def __init__(self, data):
    self.data = data

# Main class
def main():
  ##### Testing out the classes
  # size = 10
  # m = Graph(size=10)
  # m.addEdge(1, 1)
  # print(m)
  # print(m.checkEdge(1, 1))

  # Creating node graph
  # Mirroring adjacency_matrix_4_directional
  g = Graph(5)
  g.addNode(Node("a"))
  g.addNode(Node("b"))
  g.addNode(Node("c"))
  g.addNode(Node("d"))
  g.addNode(Node("e"))

  g.addEdge(0, 1)
  g.addEdge(1, 2)
  g.addEdge(2, 3)
  g.addEdge(2, 4)
  g.addEdge(4, 0)
  g.addEdge(4, 2)
  print(g)
  print(g.checkEdge(2, 3)) # checks for row C edge column D edge

# Anchor
if __name__ == "__main__":
  main()