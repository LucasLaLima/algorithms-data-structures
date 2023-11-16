def merge_sort(l):
  if len(l) <= 1:
    return l
  
  # Split
  left, right = split(l)
  # Merge_sort
  left = merge_sort(left)
  right = merge_sort(right)
  # Merge
  return merge(left, right)
  
def split(l):
  mid = len(l)//2
  left = l[:mid]
  right = l[mid:]
  return left, right

def merge(left, right):
  res = []
  i = 0
  j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      res.append(left[i])
      i+=1
    else:
      res.append(right[j])
      j+=1
  
  while i < len(left):
    res.append(left[i])
    i+=1
  
  while j < len(right):
    res.append(right[j])
    j+=1

  return res

#####
# Executable
#####
a = [5, 6, 12, 99, 3, 1, 12, 14]
# a = [3, 2 ,1]
b = merge_sort(a)
print(b)
