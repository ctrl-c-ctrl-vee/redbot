class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def _hash_function(self, key):
        return sum(ord(char) for char in str(key)) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)  # Update existing key
                    return
            self.table[index].append((key, value))  # Add new key-value pair

    def search(self, key):
        index = self._hash_function(key)
        bucket = self.table[index]
        if bucket is None:
            return None
        for k, v in bucket:
            if k == key:
                return v
        return None

# Example usage
ht = HashTable()
ht.insert("apple", 5)
ht.insert("banana", 3)
ht.insert("cherry", 7)

print(ht.search("banana"))  # Output: 3
print(ht.search("orange"))  # Output: None
