"""
Bubble Up & Bubble Down
- Bubble Up: sorts durning heap build
- Bubble Down: sorts after heap is constructed; also known as heapify

Runs in O(n^2)
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
    # If we have to make an exchange, sorted is false
    if a[i] > a[i+1]:
      sorted = False
      # print(f"Switching: {a[i]} & {a[i+1]}")
      a[i], a[i+1] = a[i+1], a[i]
  # print(f"Current state of a: {a}")
print(f"Sorted a: {a}")