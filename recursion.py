# Non-recusive method
def sum(numbers):
  total = 0
  for number in numbers:
    total+=number
  return total

def sum_recursion(numbers):
  if not numbers:
    return 0
  print("Calling sum(%s)" % numbers[1:])
  remaining_sum = sum_recursion(numbers[1:])
  print("Call to sum(%s) returning %d + %d" % (numbers, numbers[0], remaining_sum))
  return numbers[0] + remaining_sum

def main():
  a = [1,2,3]
  print(sum(a))
  print(sum_recursion(a))

if __name__ == "__main__":
  main()
