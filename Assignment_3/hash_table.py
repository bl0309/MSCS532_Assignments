class HashTable:
    def __init__(self, capacity=8, load_factor_threshold=0.75):
        """
        1. Initialize buckets and parameters.
        """
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]
        self.load_factor_threshold = load_factor_threshold

    def _hash(self, key):
        """
        2. Compute bucket index.
        """
        return hash(key) % self.capacity

    def insert(self, key, value):
        """
        3. Insert or update key-value pair.
        """
        idx = self._hash(key)
        bucket = self.buckets[idx]

        # Update existing key
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Otherwise append new key
        bucket.append((key, value))
        self.size += 1

        # Resize if load factor too high
        if self.size / self.capacity > self.load_factor_threshold:
            self._resize()

    def search(self, key):
        """
        4. Retrieve value for key, or None.
        """
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        """
        5. Remove key-value pair; return True if removed.
        """
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def _resize(self):
        """
        6. Double capacity and re-hash all entries.
        """
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self.insert(key, value)  # re-inserts and updates size

    def __len__(self):
        """Return number of elements."""
        return self.size

    def __repr__(self):
        """String representation for debugging."""
        pairs = []
        for bucket in self.buckets:
            for k, v in bucket:
                pairs.append(f"{k!r}: {v!r}")
        return "{" + ", ".join(pairs) + "}"


# Testing the HashTable
if __name__ == "__main__":
    ht = HashTable()

    # Insert some entries
    for i in range(20):
        ht.insert(f"key{i}", i)
    print("After inserts:", ht)
    print("Current size:", len(ht), "Capacity:", ht.capacity)

    # Search for existing and missing keys
    print("Search key5 ->", ht.search("key5"))
    print("Search missing ->", ht.search("does_not_exist"))

    # Delete a few keys
    print("Delete key5 ->", ht.delete("key5"))
    print("Delete missing ->", ht.delete("does_not_exist"))
    print("After deletes:", ht)
    print("Current size:", len(ht), "Capacity:", ht.capacity)

    # Trigger resizing by inserting more elements
    for i in range(20, 50):
        ht.insert(f"key{i}", i)
    print("After more inserts (resize should happen):")
    print("Size:", len(ht), "Capacity:", ht.capacity)
    print(ht)
