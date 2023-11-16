"""
Poor alogrithm for sorting.
Randomizes order of list until list is sorted.
Unreliable iteration count in the attempts variable.
"""
import random

def is_sorted(lst):
  """
  Verifying function.
  """
  for index in range(len(lst)-1):
    if lst[index] > lst[index+1]:
      return False
  return True

def bogo_sort(lst):
  attempts = 0
  while not is_sorted(lst):
    random.shuffle(lst)
    attempts += 1
    print(attempts)
  return lst

def main():
  numbers = [5, 8, 1, 4, 7]
  print(bogo_sort(numbers))

if __name__ == "__main__":
  main()