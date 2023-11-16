def recursive_binary_search(ls, target):
  if not ls:
    return False
  
  midpoint = len(ls) // 2

  if ls[midpoint]==target:
    return True
  
  if ls[midpoint] < target:
    return recursive_binary_search(ls[midpoint+1:], target)
  else:
    return recursive_binary_search(ls[:midpoint], target)

def verify(index):
  if index is not None:
    print("Target found.")
  else:
    print("Target not found.")

# Execution
if __name__ == "__main__":
  # Input values
  target = 6
  list_length = 10

  # Algo
  numbers = [x for x in range(1, list_length+1)]
  result = recursive_binary_search(numbers, target)
  verify(result)