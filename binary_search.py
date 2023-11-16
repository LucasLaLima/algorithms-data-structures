def binary_search(ls, target):
  """
  Returns the index position of the target if found, else returns None
  """
  first = 0
  last = len(ls)-1
  while first <= last:
    mid = (last + first)//2 # floor division
    if ls[mid] > target:
      last = mid-1 
    elif ls[mid] < target:
      first = mid+1
    else:
      return mid
    return None
  
def verify(index):
  if index is not None:
    print(f"Target found at index: {index}")
  else:
    print("Target not found in list.")

# Execution
if __name__ == "__main__":
  # Input values
  target = 12
  list_length = 10

  # Algo
  numbers = [x for x in range(1, list_length+1)]
  result = binary_search(numbers, target)
  verify(result)