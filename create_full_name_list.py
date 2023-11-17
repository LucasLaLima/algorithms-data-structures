from random import randint

def main():
  n = []
  # Stores first names
  with open("first-names.txt", "r") as f:
    for line in f:
      n.append(line.strip())
  
  # Creates full names
  full_names = []
  while len(n)>=2:
    first_name = n.pop(0)
    last_name = n.pop(0)
    full_names.append(f"{first_name} {last_name}")

  # Print each name randomly 
  for i in range(0, len(full_names)):
    index = randint(0, len(full_names)-1)
    print(full_names.pop(index))

if __name__ == "__main__":
  main()