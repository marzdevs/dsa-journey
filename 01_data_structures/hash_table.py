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

        # Step 3: Clear out old duplicates if they exist
        for k, v in bucket:
            if k == key:
                bucket.remove((k, v))
                break

        # Step 4: Add the fresh key-value pair
        bucket.append((key, value))

    def get(self, key):
        # Step 1: Find the bucket index using our hash function
        index = self._hash_function(key)
        # Step 2: Grab the specific bucket
        bucket = self.table[index]

        # Step 3: Search the bucket
        for k, v in bucket:
            if k == key:
                return v
        # Step 4: The loop finished and found nothing
        return "key not found"

    def remove(self, key):
        # Step 1: Find the bucket index using our hash function
        index = self._hash_function(key)
        # Step 2: Grab the specific bucket
        bucket = self.table[index]

        # Step 3: Loop through the bucket
        for k, v in bucket:
            if k == key:
                bucket.remove((k, v))
                return f"Deleted {key}"

        # Step 4: Loop finished without breaking, so key wasn't there
        return "Key not found"

# --- TEST SUITE FOR YOUR HASH TABLE ---
if __name__ == "__main__":
    # 1. Initialize a small table of size 10 to test our modulo math
    print("Initializing HashTable...")
    ht = HashTable()

    # 2. Test Inserting fresh data
    print("\n--- Testing Insert ---")
    ht.insert("apple", 5)
    ht.insert("banana", 2)
    ht.insert("cherry", 7)
    print("Inserted 'apple': 5, 'banana': 2, 'cherry': 7")

    # 3. Test Getting data out
    print("\n--- Testing Get ---")
    print(f"Get 'apple': {ht.get('apple')}")  # Should print: 5
    print(f"Get 'banana': {ht.get('banana')}")  # Should print: 2

    # 4. Test Updating an existing key (The Duplicate Cleanup Step)
    print("\n--- Testing Update (No Duplicates) ---")
    ht.insert("apple", 10)  # Changing apple from 5 to 10
    print(f"Get updated 'apple': {ht.get('apple')}")  # Should print: 10

    # 5. Test Missing Keys
    print("\n--- Testing Missing Keys ---")
    print(f"Get non-existent 'grape': {ht.get('grape')}")  # Should print: key not found

    # 6. Test Deletion
    print("\n--- Testing Remove ---")
    print(ht.remove("banana"))  # Should print a success or run smoothly
    print(f"Get deleted 'banana': {ht.get('banana')}")  # Should print: key not found

    # 7. Test Deleting a key that isn't there
    print("\n--- Testing Remove Missing Key ---")
    print(ht.remove("grape"))  # Should handle gracefully without crashing
