"""
Binary Tree is a tree where each node has no more than 2 children.

Binary Search Trees ensure that every parent is greater than one child and less than the other child.

Starting at root nodes, the left-most child should be the smallest value in the set/tree. The right-most child should be the largest value in the set/tree.

Runtime complexity: O(log n) (optimally)
Worse case: O(n) # depending how balanced it is

They help locate nodes when the BSTs are in order.
"""

class Node:
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self, root=None):
    self.root = root

  def insert(self, node):
    self.root = self.insertHelper(self.root, node)
    return
  
  def insertHelper(self, root, node):
    """
    Used for recursion purposes
    """
    if not root:
      # Empty root pointer
      root = node
      return root
    elif node.value < root.value:
      # If node is less than root pointer, check left child
      root.left = self.insertHelper(root.left, node)
    else:
      # If node is greater than root, check right child
      root.right = self.insertHelper(root.right, node)
    return root

  def display(self):
    self.displayHelper(self.root)
    return
  
  def displayHelper(self, root):
    # Ascending order print
    # Replace left - right below to get decending order
    if root:
      # debug
      # print(f"Cur: {root.value}")
      # print(f"Left: {root.left}")
      # print(f"Right: {root.right}")
      # print("")
      self.displayHelper(root.left)
      print(root.value)
      self.displayHelper(root.right)
    return
  
  def search(self, value):
    return self.searchHelper(self.root, value)

  def searchHelper(self, root, value):
    if not root:
      return False
    elif root.value == value:
      return True
    elif root.value > value:
      return self.searchHelper(root.left, value)
    else:
      return self.searchHelper(root.right, value)
    
  def remove(self, value):
    if self.search(value):
      self.removeHelper(self.root, value)
    else:
      print(f"Data: {value} could not be found in BST.")
    return

  def removeHelper(self, root, value):
    if not root:
      return root
    elif value < root.value:
      root.left = self.removeHelper(root.left, value)
    elif value > root.value:
      root.right = self.removeHelper(root.right, value)
    else: # Found node we want to remove
      # If leaf node (bottom row of tree)
      if not root.left and not root.right:
        root = None
      elif root.right: # Need to find successor
        root.value = self.successor(root)
        root.right = self.removeHelper(root.right, root.value)
      else: # root.left != None; Need to find predecessor
        root.value = self.predecessor(root)
        root.left = self.removeHelper(root.left, root.value)
    return root

  def successor(self, root):
    """
    Helps find the least value below the right child of this root node
    """
    root = root.right
    while root.left:
      root = root.left
    return root.value

  def predecssor(self, root):
    """
    Helps find the greatest value to the left of/less than this root node
    """
    root = root.left
    while root.right:
      root = root.right
    return root.value

def main():
  # Initialization
  bst = BinarySearchTree()

  # Inserting nodes
  bst.insert(Node(5))
  bst.insert(Node(1))
  bst.insert(Node(9))
  bst.insert(Node(2))
  bst.insert(Node(7))
  bst.insert(Node(3))
  bst.insert(Node(6))
  bst.insert(Node(4))
  bst.insert(Node(8))

  # Displaying tree
  # bst.display()

  # Searching
  # found = bst.search(10) # False
  # found = bst.search(7) # True
  # print(found)

  # Removing
  # bst.remove(0) # Data: 0 could not be found in BST.
  bst.remove(2) # works
  bst.display()

if __name__ == "__main__":
  main()