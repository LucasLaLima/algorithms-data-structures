"""
Selection sort uses two arrays: unsorted, sorted. 
Each pass of the unsorted array stores the smallest value and places it in the sorted array.
It looks across entire unsorted array with each pass.

This algorithm is better than bogo sort but is still slow.

As shown on an input of 10,000 numbers, it runs fairly slow (~12 s).
An input of 1M inputs runs in 

Run time is O(n^2)
"""

def selection_sort(values):
  sorted_list = []
  print("%-25s %-25s" % (values, sorted_list))
  for i in range(0, len(values)):
    index_to_move = index_of_min_val(values)
    sorted_list.append(values.pop(index_to_move))
    print("%-25s %-25s" % (values, sorted_list))
  return sorted_list

def index_of_min_val(values):
  min_index = 0
  for i in range(1, len(values)):
    if values[i] < values[min_index]:
      min_index = i
  return min_index

def main():
  numbers = [1, 24, 5, 6, 3, 8, 12]
  print(selection_sort(numbers))

if __name__ == "__main__":
  main()