"""
Heap Queues (ie. 'heapq') are used to represent priority queues in Python.
The property of this data structure in Python is that, each time, the smallest heap element is popped.
This is called a min-heap.

Whenever elements are pushed/popped, heap strucutre is mantained.

Thus, heap[0] returns the smallest element each time.

Pros of using heap:
- Efficient, usually O(log n)
- Space-efficient
- Easy to use

Disadvantages:
- Simple data structures
- Can't access middle elements efficiently
- No alternate sorting
- Not thread-safe; not suitable for multi-thread applications where data synchronization is critical
"""

import heapq

l = [5, 7, 9, 1, 3]
# Sort list by values
heapq.heapify(l)
print(l)

# Using heappush() to push elements into heap
heapq.heappush(l, 4)
print(l)

# Using heappop() to pop smallest element
print(heapq.heappop(l))
print(type(l))
print(l)

# Heapppushpop(heap, element)
# Insert the element into the heap, then pop
# Increases efficency
print(heapq.heappushpop(l, 2))

# Heapreplace(heap, element)
# Inserts and pops elements in one statement, but slightly different.
# Element is first popped, then element is pushed
# Thus a value larger than the pushed value can be returned
print(heapq.heapreplace(l, 2))

# nlargest, returns n largest values in heap
# The heap remains unchanged
print(heapq.nlargest(3,l))

# nsmallest, returns n smallest values in heap
# The heap remains unchanged
print(heapq.nsmallest(3,l))

"""
Bubble Up & Bubble Down
- Bubble Up: sorts during heap build
- Bubble Down: sorts after heap is constructed; also known as heapify
"""

a = [5, 3, 8, 1, 2, 6, 9, 4, 7]

# Bubble sort
# Orders input list in ascending order by comparing two values at any given time
sorted = False
while not sorted:
  # print(f"Starting a: {a}")
  # switches_count = 0
  sorted = True
  for i in range(len(a)-1):
    if a[i] > a[i+1]:
      sorted = False
      # print(f"Switching: {a[i]} & {a[i+1]}")
      a[i], a[i+1] = a[i+1], a[i]
  # print(f"Current state of a: {a}")
print(f"Sorted a: {a}")
  

      
