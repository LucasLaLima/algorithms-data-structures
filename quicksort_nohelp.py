def quicksort(a):
  if len(a) <= 1:
    return a

  pivot = a[0]
  left = []
  right = []
  for i in range(1, len(a)):
    if a[i] < pivot:
      left.append(a[i])
    else:
      right.append(a[i])
  return quicksort(left) + [pivot] + quicksort(right)

def main():
  # numbers = [1, 5, 0, 25, 12, 47, 30, 101, 50]
  numbers = [4, 6, 3, 2, 9,  7, 3, 5]
  print(quicksort(numbers))

if __name__ == "__main__":
  main()