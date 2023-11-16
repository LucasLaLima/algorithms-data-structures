def merge_sort(lst):
  """
  Sorts a list in acending order.
  Returns a new sorted list.
  Steps:
  1) Divide: Find the midpoint of the list and divide into sublists
  2) Conquer: Recursively sort the sublists created in previous steps.
  3) Combine: Merge the sorted sublists created in previous step.

  Overall runtime is O(n * log(n)) time.

  Given python split runtime addendum:
  Overall runtime is O(k*n*log(n)) time. [Which is much more expensive]

  Linear space complexity. Only newly requested memory is when storing the newly sorted list
  into a new variable.
  """

  # Naviely sorted
  if len(lst)<=1:
    return lst

  left_half, right_half = split(lst)
  left = merge_sort(left_half)
  right = merge_sort(right_half)
  return merge(left, right)

# 1) The Divide function
def split(lst):
  """
  Divide the unosrted list at midpoint into sublists.
  Returns two sublists - left and right
  Takes overall O(log(n)) time.

  However, python split method runs in a time relative to the side of the slice: k

  Thus, the ACTUAL runtime of this implementation is
  O(k * log(n)) time.
  """
  mid = len(lst)//2
  left = lst[:mid]
  right = lst[mid:]
  return left, right

def merge(left, right):
  """
  Merges two lists (arrays), sorting them in the process
  Returns a new merged list.
  Runs in overall O(n) time
  """
  l = []
  i = 0 # Left index array
  j = 0 # Right index array

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      l.append(left[i])
      i+=1
    else:
      l.append(right[j])
      j+=1

  # Handles odd number of elements in master list
  while i < len(left):
    l.append(left[i])
    i+=1
  
  while j < len(right):
    l.append(right[j])
    j+=1
  return l

def verify_sorted(lst):
  n = len(lst)
  if n == 0 or n == 1:
    return True
  return lst[0] < lst[1] and verify_sorted(lst[1:])

#################
# Exectution
#################

# l = [54, 26, 62, 93, 17, 77, 311, 44, 55, 20]
# l = merge_sort(l)
# print(l)

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(verify_sorted(alist))
blist = merge_sort(alist)
print(verify_sorted(blist))