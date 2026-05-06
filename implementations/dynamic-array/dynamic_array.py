class DynamicArray:

    def __init__(self):

        # total capacity
        self.capacity = 4

        # number of actual items
        self.size = 0

        # underlying array
        self.data = [None] * self.capacity

    def append(self, value):

        # resize if full
        if self.size == self.capacity:
            self.resize()

        # insert item
        self.data[self.size] = value

        # increase size
        self.size += 1

    def resize(self):

        print("Resizing...")

        # double capacity
        self.capacity *= 2
        # create new bigger array
        new_data = [None] * self.capacity

        # copy old items
        for i in range(self.size):
            new_data[i] = self.data[i]

        # point data to new array
        self.data = new_data

    def print_array(self):

        print("Array:", self.data)
        print("Size:", self.size)
        print("Capacity:", self.capacity)


# =========================
# TESTING
# =========================

arr = DynamicArray()

arr.print_array()

arr.append(10)
arr.append(20)
arr.append(30)
arr.append(40)

print("\nAfter adding 4 items:")
arr.print_array()

arr.append(50)

print("\nAfter adding 5th item:")
arr.print_array()