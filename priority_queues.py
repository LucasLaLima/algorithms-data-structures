"""
Priorty queues are abstract data types and a special form of queues. 

Based on their characteristic priority, the first element in the PQ should have he highest priority.

Basic operations with PQ:
- is_empty (boolean return)
- insert (element is inserted considering its priority)
- pop (first element; ie. highest priority)

Commonly used for scheduling.
If two elements have the same priority, they are stored in the order they are introudced to the PQ.

"""

import time
import heapq as hq

jobs = [(2, 'task_1'), 
(5, 'task_2'),
(1, 'task_4'), 
(4, 'task_5'),
(3, 'task_3'),
(1, 'task_8')
]

interrupts = [
  (1, 'intr_1'),
  (2, 'intr_2'),
  (13, 'intr_3')
]

i, j = 0, 0

hq.heapify(jobs)
print(jobs)

# Scheduling the tasks
while len(jobs) != 0 :
  next_job = jobs[0][1]
  priority = jobs[0][0]
  print(f"Looking at: {next_job}\nPriority: {priority}")

  # Emulate servicing the task
  # for _ in range(0, 5):
  #   print(".", end="")
  #   time.sleep(0.5)

  # Pop the job that completed
  hq.heappop(jobs)

  # Adding interrupts
  if j < len(interrupts):
    hq.heappush(jobs, interrupts[j])
    print("New interrupt arrived!", interrupts[j])
    j += 1

  # Job queue after arrival of interrupt
  print("Job queue currently :", jobs)
  print("\n")

  # Emulate servicing the task
  for _ in range(0, 5):
    time.sleep(0.5)
print("\nAll interrupts and jobs completed!") 