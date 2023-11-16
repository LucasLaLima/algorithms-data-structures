l = [1, 2, 3]
# result = l[0] # access is constant time

# Accessing feature of arrays
if 1 in l:
  print(True)

for i in l:
  if i==1:
    print(True)

# Insert feature of arrays at 0th position incures highest runtime complexity
# Appends don't incure the same runtime complexity
numbers = []
numbers.append(2) # memory allocation and size of list are the same
numbers.append(200) # calls list resize and then adds new number
# resize of list in python go from 0, 4, 8, 16, 25, 35, 46
# append has ammortized constant space complexity, average of all memory allocations is constant

# Insert costs more
# Run time of O(k) where k is number of elements in new list
numbers = []
numbers.extend([4,5,6])
print(numbers)

# Delete
# Shifts every element to left; worst case is deleting 0th element; O(n) runtime