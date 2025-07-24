import time
import matplotlib.pyplot as plt
import random

# Separate Chaining Hash Table
class SeparateChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))

# Open Addressing Hash Table (Linear Probing)
class OpenAddressingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        start_idx = idx
        while self.table[idx] is not None and self.table[idx][0] != key:
            idx = (idx + 1) % self.size
            if idx == start_idx:
                raise Exception("Hash table is full")
        self.table[idx] = (key, value)

# Testing performance
def test_performance():
    load_factors = [0.2, 0.4, 0.6, 0.8, 0.95]
    table_size = 10007  # Prime number size for better distribution

    open_times = []
    chain_times = []

    for lf in load_factors:
        num_items = int(table_size * lf)
        keys = [str(random.randint(0, 1000000)) for _ in range(num_items)]

        # Open addressing
        oa = OpenAddressingHashTable(table_size)
        start = time.time()
        for key in keys:
            oa.insert(key, key)
        open_duration = time.time() - start
        open_times.append(open_duration)

        # Separate chaining
        sc = SeparateChainingHashTable(table_size)
        start = time.time()
        for key in keys:
            sc.insert(key, key)
        chain_duration = time.time() - start
        chain_times.append(chain_duration)

    return load_factors, open_times, chain_times

# Run the test and plot results
load_factors, open_times, chain_times = test_performance()

plt.figure(figsize=(10, 6))
plt.plot(load_factors, open_times, marker='o', label='Open Addressing')
plt.plot(load_factors, chain_times, marker='s', label='Separate Chaining')
plt.title('Hash Table Insertion Time vs Load Factor')
plt.xlabel('Load Factor')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
