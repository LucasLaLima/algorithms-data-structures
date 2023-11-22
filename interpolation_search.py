"""
Improvement over binary search best used for "uniformly" distributed "guesses" where a value might be based on a calculated probe results. 

If probe is incorrect, search area is narrowed; and a new probe is selected.

average case runtime: O (log ( log n ) )
worse case: O (n) 
- Worst case happens when values increase exponentially

It's better than binary serach's approach of always taking the middle value.

"""

def interpolationSearch(array, value):
  # Calculate bounds of lst
  high = len(array)-1
  low = 0

  while value >= array[low] and value <= array[high] and low <= high:
    # Interpolation sort formula
    probe = low + (high - low) * (value - array[low]) // (array[high] - array[low])
    print(f"This is our guess: {probe}")
    if array[probe] == value:
      return probe
    elif array[probe] < value:
      low = probe + 1
    else:
      high = probe - 1
  return -1


# a = [
#   1,
#   2,
#   3,
#   4,
#   5,
#   6,
#   7,
#   8,
#   9
# ]

b = [
  1,
  2,
  4,
  8,
  16,
  32,
  64,
  256,
  512,
  1026
]

targetValue = 256
index = interpolationSearch(b, targetValue) 
if index != -1:
  print(f"Element found at: {index}")
else:
  print("Element not found.")