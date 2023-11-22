"""
Queus are FIFO data structures.
First in first out
"""

from collections import deque
d = deque()
d.append(1)
d.append(2)
# Inserts at (index, value)
d.insert(1, 3) # [1, 3, 2]
d.append(1)
# Counts number of elements equal to value
print(d.count(1)) # 2
# Inserts at head of queue
d.appendleft(5)
# Flips queue
d.reverse()
# Extends queue by elements of given iterable object
d.extend([7, 8])
# Pops from tail of queue
print(d) # deque([1, 2, 3, 1, 5, 7, 8])
tail = d.pop()
print(d) # deque([1, 2, 3, 1, 5, 7])
head = d.popleft()
print(d) # deque([2, 3, 1, 5, 7])