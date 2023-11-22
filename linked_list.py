# Linked lists are better at inserting and deleting than arrays
# First node is linked list is head
# Last node is called tail
# Nodes are self-referential objects

class Node:
  """
  An object for storing a singel node of a linked list.
  Models two attributes - data and teh link to the next node in the list.
  """
  def __init__(self, data):
    self.data = data
    self.next_node = None
  
  def __repr__(self):
    return f"<Node data: {self.data}>"

class LinkedList:
  """
  Singly linked list
  """
  def __init__(self):
    self.head = None
  
  def is_empty(self):
    return self.head==None

  def size(self):
    """
    Returns number of nodes, takes O(n) time
    """
    current = self.head
    count = 0
    while current:
      count += 1
      current = current.next_node
    return count

  def add(self, data):
    """
    Adds a new node at the head of the list
    This operation takes O(1) time
    """
    new_node = Node(data)
    new_node.next_node = self.head
    self.head = new_node
    return

  def search(self, key):
    """
    Return first node containing data that matches the key.
    Returns the node or 'None' if not found.
    Takes O(n) run time.
    """
    current = self.head

    while current:
      if current.data == key:
        return current
      else:
        current = current.next_node
    return None

  def insert(self, data, index):
    """
    Inserts a new Node containing data at index position
    Insertion takes O(1) but finding node at insertion
    point takes O(n).

    Therefore it takes O(n).
    """
    if index==0:
      self.add(data)
    
    if index > 0:
      new = Node(data)
      position = index
      current = self.head

      # Finds node pointing to target position
      while position > 1:
        current = current.next_node
        position -= 1

      # Breaks pointers for insertion
      right_neighbor = current.next_node
      left_neighbor = current

      # Insertion
      left_neighbor.next_node = new
      new.next_node = right_neighbor
    return

  def remove(self, key):
    """
    Removes node in linked list as with value that matches key.
    Returns None if key doesn't exist.
    Takes O(n) times.
    """
    current = self.head
    previous = None
    found = False
    
    while current and not found:
      if current.data == key and current is self.head:
        found = True
        self.head = current.next_node
      elif current.data == key:
        found = True
        previous.next_node = current.next_node # skipping over current node
      else:
        previous = current
        current = current.next_node
    return current

  def node_at_index(self, index):
    if index == 0:
      return self.head
    
    current = self.head
    position = 0
    while position < index:
      current = current.next_node
      position +=1
    return current

  def __repr__(self):
    nodes = []
    current = self.head
    while current:
      if current is self.head:
        nodes.append(f"[Head: {current.data}]")
      elif current.next_node is None: # tail
        nodes.append(f"[Tail: {current.data}]")
      else:
        nodes.append(f"[{current.data}]")
      
      current = current.next_node
    return "->".join(nodes)

# Execution
def main():
  # Node creation
  # n1 = Node(10)
  # n2 = Node(20)
  # n3 = Node(30)

  # Linked list creation
  l = LinkedList()

  # Linked list appending
  l.add(1)
  l.add(2)
  l.add(3)
  l.add(4)

  # Functions
  # print(l.size())
  # print(l)
  # x = l.search(3)
  # print(x)

  # Linked lists are superior to lists/arrays in insertion and deletion time
  # Simply need to update before and after pointers to new node where you want to insert
  # However, finding the index where you want to introduce the new node is O(n)
  print(l)
  l.insert(5, 3)
  print(l)
  l.remove(3)
  print(l)

if __name__ == "__main__":
  main()