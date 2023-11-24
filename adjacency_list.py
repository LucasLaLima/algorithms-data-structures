"""
Adjacency lists are arrays full of linked lists.
Each linked list has a unique node at the head.
All adjacent neighbors to that node are added to that node's linked list.

Runtime complexity to check an edge: O(v)
Space complexity: O(v+e)
"""

from linked_list import LinkedList

# Node class
class Node:
  def __init__(self, data):
    self.data = data

# Graph class
class Graph:
  def __init__(self):
    self.alist = []
  
  def addNode(self, node):
    curList = LinkedList()
    curList.add(node)
    self.alist.append(curList)
    return
  
  def addEdge(self, src, dst):
    curList = self.alist[src]
    dstNode = self.alist[dst].head
    curList.add(dstNode)
    return
  
  def checkEdge(self, src, dst):
    curList = self.alist[src]
    dstNode = self.alist[dst].head
    cur = curList.head
    while cur!=None:
      if cur == dstNode:
        return True
      cur = cur.next_node
    return False

  def print(self):
    for a in self.alist:
      print(a)
    return
    
# Main class
def main():
  g = Graph()
  
  # Nodes from adjacency_list_4
  g.addNode(Node('A'))
  g.addNode(Node('B'))
  g.addNode(Node('C'))
  g.addNode(Node('D'))
  g.addNode(Node('E'))

  g.addEdge(0, 1)
  # print(g.checkEdge(0, 1))
  g.print()
  return

# Anchor
if __name__ == "__main__":
  main()