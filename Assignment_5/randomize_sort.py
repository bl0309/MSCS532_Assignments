import random
import time
import matplotlib.pyplot as plt
import pandas as pd

# Deterministic Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Randomized Quicksort
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

# Input generator
def generate_input(size, distribution='random'):
    if distribution == 'random':
        return [random.randint(0, size) for _ in range(size)]
    elif distribution == 'sorted':
        return list(range(size))
    elif distribution == 'reverse':
        return list(range(size, 0, -1))

# Benchmarking
def benchmark_sorting_algorithms(sizes, distribution):
    deterministic_times = []
    randomized_times = []
    for size in sizes:
        arr = generate_input(size, distribution)
        start = time.time()
        quicksort(arr.copy())
        deterministic_times.append(time.time() - start)

        start = time.time()
        randomized_quicksort(arr.copy())
        randomized_times.append(time.time() - start)
    return deterministic_times, randomized_times

# Sizes to test
sizes = [100, 500, 1000, 2000, 5000]

# Run all benchmarks
random_det, random_rand = benchmark_sorting_algorithms(sizes, 'random')
sorted_det, sorted_rand = benchmark_sorting_algorithms(sizes, 'sorted')
reverse_det, reverse_rand = benchmark_sorting_algorithms(sizes, 'reverse')

# Plot performance for random inputs
plt.plot(sizes, random_det, label='Deterministic Quicksort')
plt.plot(sizes, random_rand, label='Randomized Quicksort')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Performance on Random Input')
plt.legend()
plt.grid(True)
plt.show()

# Tabular summary
df = pd.DataFrame({
    'Input Size': sizes,
    'Deterministic (Random)': random_det,
    'Randomized (Random)': random_rand,
    'Deterministic (Sorted)': sorted_det,
    'Randomized (Sorted)': sorted_rand,
    'Deterministic (Reverse)': reverse_det,
    'Randomized (Reverse)': reverse_rand,
})

print(df.to_string(index=False))
