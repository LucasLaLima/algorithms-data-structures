"""
Quicksort relies on recursion.

It keeps calling itself with smaller and smaller subsets of input.

Algorithm:
- Take first value as pivot
- Create 'left-list' that has all values less than pivot
- Create 'right-pivot' that has all values greater than pivot
- Put 'left-list' into quicksort function
- Put 'right-list' into quicksort function
- Return quicksort(left) + [pivot] + quicksort(right)

With 1M inputs, runtime is about 11 seconds.

Worst case: Runtime is O(n^2) in worst case, where the list is sorted backwards.

Best case: Pivot is value median of entire list.

In general, runtime for quicksort improves to O(n log n) when pivots are chosen at random and averaged over many runs.
"""

def quicksort(values):
  # Base case
  if len(values) <= 1:
    return values
  
  # Divide and conquor
  pivot = values[0] # Choosing this value can be crucial to runtime
  less_than_pivot = []
  greater_than_pivot = []
  for v in values[1:]:
    if v <= pivot:
      less_than_pivot.append(v)
    else:
      greater_than_pivot.append(v)
  # print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))
  return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

def main():
  # numbers = [1, 5, 0, 25, 12, 47, 30, 101, 50]
  numbers = [4, 6, 3, 2, 9,  7, 3, 5]
  print(quicksort(numbers))

if __name__ == "__main__":
  main()