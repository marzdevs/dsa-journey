class HashTable:
    def __init__(self):
        # 1. Store the size of the table
        self.size = 10

        # 2. Create a list containing 10 individual empty lists
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        # 1. Start a total at 0
        total = 0
        # 2. Loop through every character and add its number code
        for char in str(key):
            total += ord(char)
        # 3. Use modulo to make it fit our table size
        return total % self.size

    def insert(self, key, value):
        # Step 1: Find the bucket index using our hash function
        index = self._hash_function(key)
        # Step 2: Grab the specific bucket
        bucket = self.table[index]