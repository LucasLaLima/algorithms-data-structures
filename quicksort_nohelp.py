def quicksort(l):
  if len(l) <= 1:
    return l
  
  pivot = l[0]
  left = []
  right = []
  for i in l[1:]:
    if i < pivot:
      left.append(i)
    else:
      right.append(i)
  return quicksort(left) + [pivot] + quicksort(right)

def main():
  # numbers = [1, 5, 0, 25, 12, 47, 30, 101, 50]
  numbers = [4, 6, 3, 2, 9,  7, 3, 5]
  print(quicksort(numbers))

if __name__ == "__main__":
  main()