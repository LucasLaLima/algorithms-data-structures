from quicksort import quicksort

def binary_search(l, target):
  first = 0
  last = len(l)-1
  while first <= last:
    midpoint = (last+first)//2
    if l[midpoint] == target:
      return midpoint
    elif l[midpoint] < target: # aka "too small"
      first = midpoint+1
    else: # l[midpoint] > target aka "too big"
      last = midpoint-1
  return None # Coulnd't find match

def main():
  # Store full names at random
  full_names = []
  with open("random-full-names.txt", "r") as f:
    for n in f:
      full_names.append(n.strip())

  # Sort full names by letter
  sorted_full_names = quicksort(full_names)

  # Stealing target name from full-names.txt (the sorted file)
  target_name = "Rakel Ralina" # Line 2000
  target_index = binary_search(sorted_full_names, target_name) + 1 # File starts at 1, indexes start at 0
  print(target_index)

if __name__ == "__main__":
  main()