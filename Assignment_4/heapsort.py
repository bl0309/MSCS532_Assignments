import matplotlib.pyplot as plt
import time
import random

# Heapsort implementation
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Benchmark and generate graph
sizes = [1000, 2000, 4000, 8000, 16000, 32000]
times = []

for size in sizes:
    arr = [random.randint(1, size) for _ in range(size)]
    start_time = time.perf_counter()
    heapsort(arr)
    end_time = time.perf_counter()
    times.append(end_time - start_time)

# Plotting the graph
plt.figure(figsize=(8, 5))
plt.plot(sizes, times, marker='o')
plt.title("Heapsort Runtime vs Input Size")
plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.grid(True)
plt.tight_layout()
plt.show()
