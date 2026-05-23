from array import *
"""
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


for i in range(len(vals)): # range gets index of arr and loops index size
    print(vals[i])
"""

import ctypes
class DynamicArray(object):
    # constructor method complexity: 0(1)
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A=self._make_array(self.capacity)

    # complexity: 0(1)
    def __len__(self):
        # len(obj)
        return self.n

    # complexity: 0(1)
    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return "IndexError: DynamicArray index out of range"

    # complexity: 0(n)
    def __delitem__(self, index):
        if 0 <= index < self.n:
            #delete
            for i in range(index, self.n-1):
                self.A[i] = self.A[i+1]
            self.n -= 1
        else:
            return "IndexError"

    # complexity: 0(n) two nested loops. one searches for elements O(n) other shifts elements to overwrite.
    # O(n) so O(n + n) is O(n)
    def remove(self, element):
        flag = 0
        for i in range(self.n):
            if self.A[i] == element:
                flag = 1
                for j in range(i,self.n-1):
                    self.A[j] = self.A[j+1]
                self.n -= 1
                break
        if flag == 0:
            print("Element not found")

    # complexity: 0(1) altho it calls resize method which is O(n) because capacity doubles ech time. the resizing happens less frequently.
    def append(self, item):
        if self.n == self.capacity: #cap = size full
            self.resize(2 * self.capacity) # double the capacity by resizing
        self.A[self.n] = item #adds new item to end of array
        self.n += 1

    # complexity: 0(n) for loop shifts items..if inserting 0 all items in index after 0 shift to right.
    def insert(self, index, item):
        if 0 <= index < self.n:
            # do insertion
            if self.n == self.capacity:
                self.resize(2 * self.size)

            for i in range(self.n - 1, index - 1, -1):
                self.A[i+1] = self.A[i]
            self.A[index] = item
            self.n += 1

        else:
            return "IndexError"

    # complexity: 0(1)
    def pop(self):
        self.n -= 1

    # complexity: 0(1)
    def clear(self):
        self.n=0
        self.capacity= 1

    # complexity: 0(n) if item is last in index must check all indexes
    def find(self,item):
        print(f"Finding index of {item}...")

        for i in range(self.n):
            if self.A[i] == item:
                return i
        return "Value not in list"

    # complexity: 0(n)
    def resize(self, new_capacity):
        #create new array with large capacity
        B = self._make_array(new_capacity)
        self.capacity = new_capacity

        #copy content
        for i in range(self.n):
            B[i] = self.A[i]
        #reassign
        self.A = B

    # complexity: 0(1) calls return
    def _make_array(self, new_capacity):
        return(new_capacity * ctypes.py_object)()

    # able to print array in str format
    # complexity: 0(n) iterates through all elements in loop
    def __str__(self):
            if self.n == 0:
                return "[]"

            result = ""
            for i in range(self.n):
                # print every value
                result += str(self.A[i]) + ", "

            # [:-2] strips out the extra comma and space at the very end prints it
            return "[" + result[:-2] + "]"

arr = DynamicArray()

arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)
arr.append(6)

print(arr)
print("Length of array:", len(arr))
print("Element at index 0:", arr[0])
print("Element at index 1:", arr[1])
print(arr[100])

arr.insert(2,50)
print("After inserting: ", arr)

del arr[2]
print("After deleting: ", arr)

arr.remove(4)
print("After removing: ", arr)

arr.pop()
print("After pop: ", arr)


print("found at index: ", arr.find(3))



"""
class DynamicArray:
    def __init__(self):
        self.size = 0  # Elements currently in the array
        self.capacity = 1  # Total available slots
        # Create a simple list with fixed empty slots filled with None
        self.A = [None] * self.capacity

    def __len__(self):
        # Returns the number of elements: O(1)
        return self.size

    def __getitem__(self, index):
        # Returns the element at a given index: O(1)
        if not 0 <= index < self.size:
            raise IndexError("Index out of bounds!")
        return self.A[index]

    def append(self, element):
        #Adds an element to the end: Amortized O(1)
        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        self.A[self.size] = element
        self.size += 1

    def _resize(self, new_capacity):
        # Resizes the internal static array: O(n)
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
        print("Appended: %2d | Size: %2d | Capacity: %2d" % (i, len(da), da.capacity))

"""