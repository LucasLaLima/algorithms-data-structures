# Implementation of an undirected graph using Adjacency Matrix, with weighted or unweighted edges
# https://www.youtube.com/watch?v=HDUzBEG1GlA

class Vertex:
  def __init__(self, name):
    self.name = name

class Graph:
  verticies = {}
  edges = []
  edge_indices = {}

  def add_vertex(self, vertex):
    if isinstance(vertex, Vertex) and vertex.name not in self.verticies:
      self.verticies[vertex.name] = vertex
      # Add row and column of all zeros to edges matrix
      for row in self.edges:
        row.append(0)
      self.edges.append([0] * (len(self.edges)+1))
      self.edge_indices[vertex.name] = len(self.edge_indices)
      return True
    else:
      return False

  def add_edge(self, u, v, weight=1):
    if u in self.verticies and v in self.verticies:
      self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
      self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
      return True
    else:
      return False

  def print_graph(self):
    for v, i in sorted(self.edge_indices.items()):
      print(v + ' ', end="")
      for j in range(len(self.edges)):
        print(self.edges[i][j], end="")
      print(" ")

def main():
  g = Graph()
  g.add_vertex(Vertex("A"))
  g.add_vertex(Vertex("B"))
  for i in range(ord("A"), ord("K")):
    g.add_vertex(Vertex(chr(i)))
  edges = [
    "AB",
    "AE",
    "BF",
    "CG",
    "DE",
    "DH",
    "EH",
    "FG",
    "FI",
    "FJ",
    "GJ",
    "HI"
  ]

  for e in edges:
    g.add_edge(e[0], e[1])
  
  g.print_graph()
  return

if __name__ == "__main__":
  main()
