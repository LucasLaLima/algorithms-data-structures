# Implementation of adjacency Lists
# https://www.youtube.com/watch?v=HDUzBEG1GlA

class Vertex:
  def __init__(self, name):
    self.name = name
    self.neighbors = []

class Graph:
  verticies = {}

  def add_vertex(self, vertex):
    if isinstance(vertex, Vertex) and vertex.name not in self.verticies:
      self.verticies[vertex.name] = vertex
      return True
    else:
      return False

  def add_edge(self, u, v):
    if u in self.verticies and v in self.verticies:
      for key, value in self.verticies.items():
        if key == u:
          value.neighbors.append(v)
        if key == v:
          value.neighbors.append(u)
      return True
    else:
      return False
  
  def print_graph(self):
    for key in sorted(list(self.verticies.keys())):
      print(key + str(self.verticies[key].neighbors))

def main():
  g = Graph()
  a = Vertex('A')
  g. add_vertex(a)
  g.add_vertex(Vertex('S'))

  for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))
  
  edges = [
    'AB',
    'AE',
    'BF',
    'CG',
    'DE',
    'DH',
    'EH',
    'FG',
    'FI',
    'FJ',
    'GJ',
    'HI'
  ]

  for e in edges:
    g.add_edge(e[0], e[1])

  g.print_graph()
  return

if __name__ == "__main__":
  main()