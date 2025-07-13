import random
import time
import pandas as pd
import matplotlib.pyplot as plt

# Quickselect (Randomized)
def quickselect(arr, k):
    if not arr:
        raise ValueError("Array is empty")
    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

# Median of Medians (Deterministic)
def select(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]
    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(group)[len(group) // 2] for group in groups]
    pivot = select(medians, len(medians) // 2)

    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return select(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return select(highs, k - len(lows) - len(pivots))

# Benchmarking Setup
def generate_input(size, distribution):
    if distribution == "random":
        return random.sample(range(size * 3), size)
    elif distribution == "sorted":
        return list(range(size))
    elif distribution == "reverse":
        return list(range(size, 0, -1))
    else:
        raise ValueError("Unknown distribution")

def benchmark():
    sizes = [100, 1000, 10000]
    distributions = ["random", "sorted", "reverse"]
    algorithms = {
        "Quickselect": quickselect,
        "Median of Medians": select
    }
    results = []

    for size in sizes:
        for dist in distributions:
            data = generate_input(size, dist)
            for name, func in algorithms.items():
                arr_copy = data.copy()
                k = size // 2
                start = time.perf_counter()
                result = func(arr_copy, k)
                end = time.perf_counter()
                duration_ms = (end - start) * 1000

                results.append({
                    "Size": size,
                    "Distribution": dist,
                    "Algorithm": name,
                    "Time (ms)": round(duration_ms, 4),
                    "k-th Element": result
                })

    return pd.DataFrame(results)

# Main Execution
if __name__ == "__main__":
    df = benchmark()
    print("\nBenchmark Results:\n")
    print(df.to_string(index=False))

    # Plotting
    plt.figure(figsize=(12, 6))
    for size in df['Size'].unique():
        subset = df[df['Size'] == size]
        plt.bar(
            subset['Algorithm'] + " (" + subset['Distribution'] + ")",
            subset['Time (ms)'],
            label=f"n = {size}"
        )

    plt.xlabel("Algorithm and Distribution")
    plt.ylabel("Time (ms)")
    plt.title("Selection Algorithm Benchmark")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.show()
