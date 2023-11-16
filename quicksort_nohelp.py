def quicksort(values):
  if len(values) <=1:
    return values
  
  pivot = values[0]
  less_than_pivot = []
  greater_than_pivot = []
  for v in values[1:]:
    if v <= pivot:
      less_than_pivot.append(v)
    else:
      greater_than_pivot.append(v)
  return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

def main():
  # numbers = [1, 5, 0, 25, 12, 47, 30, 101, 50]
  numbers = [4, 6, 3, 2, 9,  7, 3, 5]
  print(quicksort(numbers))

if __name__ == "__main__":
  main()