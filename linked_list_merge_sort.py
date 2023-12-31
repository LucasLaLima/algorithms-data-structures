from linked_list import LinkedList

def merge_sort(linked_list):
  """
  Sorts a linked list in ascending order
  - Recursively divide the linked list into subslists containing a single node
  - Repeatedly merge the sublists to produce sorted sublists until one remains

  Returns a sorted linked list.

  Returns in O(kn log n)
  """

  if linked_list.size() == 1:
    return linked_list
  elif linked_list.head is None:
    return linked_list
  
  left_half, right_half = split(linked_list)
  left = merge_sort(left_half)
  right = merge_sort(right_half)
  return merge(left, right)

def split(linked_list):
  """
  Divide the unsorted list at midpoint into two even sub-linked lists
  Takes O(k log n)
  """
  if linked_list == None or linked_list.head == None:
    left_half = linked_list
    right_half = None
    return left_half, right_half
  
  size = linked_list.size()
  mid = size // 2
  mid_node = linked_list.node_at_index(mid-1) # Grabs middle node
  left_half = linked_list # Set left half pointer to beginning of input list
  right_half = LinkedList() # Initialize the right half linked list
  right_half.head = mid_node.next_node # Store second half of linked list to right linked list
  mid_node.next_node = None # Sever node at midpoint node
  return left_half, right_half

def merge(left, right):
  """
  Merges two linked lists, sorting by data in nodes.
  Returns a new, merged list.
  Takes O(n) time
  """

  # Create a new linked list that contains nodes from 
  # merging left and right
  merged = LinkedList()

  # Add a fake head that is discared later
  merged.add(0)

  # Set current to the head of the linked list
  current = merged.head

  # Obtain head nodes for left and right linked lists
  left_head = left.head
  right_head = right.head

  # Iterate over left and right until we reach the tail node of either

  while left_head or right_head:
    # If the head node of left is None, we're past the tail
    # Add the node from right to merged linked list
    if left_head == None:
      current.next_node = right_head
      right_head = right_head.next_node # stopping condition
    elif right_head == None:
      current.next_node = left_head
      left_head = left_head.next_node # stopping condition
    else:
      # Evaluating node that's neither head or tail of linked list
      # Obtaining node data to perform comparison operations
      left_data = left_head.data
      right_data = right_head.data
      if left_data < right_data:
        current.next_node = left_head
        left_head = left_head.next_node
      else:
        current.next_node = right_head
        right_head = right_head.next_node
    # Move current to next node (prepping to append during next loop)
    current = current.next_node
  
  #Discard fake head and set first merged node as head
  head = merged.head.next_node
  merged.head = head
  return merged

def main():
  l = LinkedList()
  l.add(10)
  l.add(2)
  l.add(44)
  l.add(15)
  l.add(200)
  print(l)
  sorted_linked_list = merge_sort(l)
  print(sorted_linked_list)

if __name__ == "__main__":
  main()