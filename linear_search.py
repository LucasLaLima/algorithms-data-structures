def linear_search(l, target):
  """
  Returns the index position of the target if found, else returns None
  """
  for i in range(0, len(l)):
    if l[i]==target:
      return i
  return None

def verify(index):
  if index is not None:
    print(f"Target found at index: {index}")
  else:
    print("Target not found in list.")

# Execution
if __name__ == "__main__":
  # Input values
  target = 8
  list_length = 10

  # Algo
  numbers = [x for x in range(1, list_length+1)]
  result = linear_search(numbers, target)
  verify(result)