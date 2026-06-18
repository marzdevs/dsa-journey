class HashTable:
    def __init__(self):
        # 1. Store the size of the table
        self.size = 10

        # 2. Create a list containing 10 individual empty lists
        self.table = [[] for _ in range(self.size)]