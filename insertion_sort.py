"""
Starting at index 1, we store a value.

We look at all indexes to the left of stored value's index.

If the values are greater than stored value, we move their index up 1

When you find a value less than stored value, you move insert stored value at the index to the right.

Runtime: O(n^2)
Best case: O(n)
"""

def insertion_sort(lst):
  for i in range(1, len(lst)):
    # print(lst)
    # print(f"Looking at index: {i}")
    cur = lst[i]
    for j in range(i-1, -1, -1):
      if lst[j] > lst[j+1]:
        lst[j], lst[j+1] = lst[j+1], lst[j]
        # print(f"Updated: {lst}")
  return lst
      

a = [
  6, 
  1,
  7,
  4,
  2,
  9,
  8,
  5,
  3
]

print(insertion_sort(a))