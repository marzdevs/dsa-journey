from array import *

vals = array('i', [5,9,8,4,2])

newArr = array(vals.typecode, ( a*a for a in vals))
print("for loop with new array")

for i in newArr:  # goes for value
    print(i)

print("while loop")
i = 0
while i<len(newArr): # initilization, check condition, and increment
    print(newArr[i])
    i+=1

"""
for i in range(len(vals)): # range gets index of arr and loops index size
    print(vals[i])
"""

import ctypes


class DynamicArray:
    def __init__(self):
        self.size = 0  # Elements currently in the array
        self.capacity = 1  # Total available slots
        # Create a simple list with fixed empty slots filled with None
        self.A = [None] * self.capacity

    def __len__(self):
        """Returns the number of elements: O(1)"""
        return self.size

    def __getitem__(self, index):
        """Returns the element at a given index: O(1)"""
        if not 0 <= index < self.size:
            raise IndexError("Index out of bounds!")
        return self.A[index]

    def append(self, element):
        """Adds an element to the end: Amortized O(1)"""
        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        self.A[self.size] = element
        self.size += 1

    def _resize(self, new_capacity):
        """Resizes the internal static array: O(n)"""
        print ("--> [RESIZE] Old capacity: %d | New capacity: %d" % (self.capacity, new_capacity))

        # 1. Allocate a brand new, larger array
        new_array = [None] * new_capacity

        # 2. Copy elements from the old array to the new one
        for i in range(self.size):
            new_array[i] = self.A[i]

        # 3. Swap the old array for the new one
        self.A = new_array
        self.capacity = new_capacity


# --- Classic 20-number simulation loop ---
if __name__ == "__main__":
    da = DynamicArray()

    for i in range(1, 21):
        da.append(i)
        print
        "Appended: %2d | Size: %2d | Capacity: %2d" % (i, len(da), da.capacity)