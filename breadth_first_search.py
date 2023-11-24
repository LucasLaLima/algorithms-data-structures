"""
Algorithm for traversing a tree or a graph data structure.

Rather than one 'branch' at a time, you traverse one 'level' at a time.

Instead of stack, we use queue.

Starting at A, we add neighbors to queue.
Then add neighbors' neighbors.
Etc.
"""

from collections import deque

"""
Given a starting point and a target/destination node, Depth First Search is a search algorithm for traversing a tree/graph data structure.

Steps:
1) Pick a route
2) Keep going until you reach a dead end or a previously visited node
3) Backtrack to last node that has unvisited adjacent neighbors.
"""
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
    self.visited = {}
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

  def depthFirstSearch(self, src):
    """
    Src is row index.
    ie. 0 => A
    ie. 1 => B and so on.
    """
    self.dFSHelper(src, self.visited)
    return

  def dFSHelper(self, src, visited):
    """
    This helper moves to the right until it hits a dead end. 
    """
    if src in visited:
      return
    else:
      visited[src] = True
      print(f"{self.nodes[src]} = visited")
    
    for i in range(len(self.matrix)):
      if self.matrix[src][i] == 1:
        # We recurse with column index as the new src
        self.dFSHelper(i, visited)
    return

  def breadthFirstSerach(self, src):
    queue = deque()
    visited = []
    queue.append(src)
    visited.append(src)

    while len(queue)!=0:
      src = queue.pop()
      print(f"{self.nodes[src]} = visited")
      for i in range(len(self.matrix)):
        if self.matrix[src][i] and i not in visited:
          queue.append(i)
          visited.append(i)
    return

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

  # g.breadthFirstSerach(0) #ABCDE
  # g.breadthFirstSerach(1) #BCEAD
  # g.breadthFirstSerach(2) #CEABD
  # g.breadthFirstSerach(3) #D
  g.breadthFirstSerach(4) #ECDAB


if __name__ == "__main__":
  main()