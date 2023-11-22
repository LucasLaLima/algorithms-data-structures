"""
In python, dynamic arrays are lists().
If you increase the size of a previous array by appending a new value; the dynamic array is reinstantiated with ~1.125 the size of the original array.
This behavior is language depended.

Advantages of dynamic arrays:
- Random access of elements; O(1)
- Good localty of reference and data cache utilization (opposite of linked lists)
- Easy to insert/delete at the ends

Disadvantags:
- Wastes a lot of smemory
- Shifting elements is O(n)
- Expanding/shrinking array is time consuming O(n) ; you need to create new array
"""