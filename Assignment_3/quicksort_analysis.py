import random
import time
import csv
import matplotlib.pyplot as plt
import pandas as pd

# Randomized Quicksort
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return randomized_quicksort(less) + equal + randomized_quicksort(greater)

# Deterministic Quicksort
def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    pivot = arr[mid]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return deterministic_quicksort(less) + equal + deterministic_quicksort(greater)

# Time Measurement
def time_sort(sort_fn, arr):
    start = time.perf_counter()
    sort_fn(arr[:])
    return time.perf_counter() - start

# Input Generator
def generate_inputs(n):
    return {
        "random": random.sample(range(n), n),
        "sorted": list(range(n)),
        "reversed": list(range(n, 0, -1)),
        "repeated": [random.choice([1, 2, 3]) for _ in range(n)],
    }

# Run Benchmarks and Save to CSV
def run_comparisons_to_csv(sizes, filename="quicksort_results.csv"):
    results = []
    for size in sizes:
        inputs = generate_inputs(size)
        for label, arr in inputs.items():
            t_rand = time_sort(randomized_quicksort, arr)
            t_det = time_sort(deterministic_quicksort, arr)
            results.append({
                "size": size,
                "input_type": label,
                "randomized_time": t_rand,
                "deterministic_time": t_det
            })
            print(f"{label.capitalize():<12} | Size: {size:<6} | Randomized: {t_rand:.5f}s | Deterministic: {t_det:.5f}s")

    # Save to CSV
    keys = results[0].keys()
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)

    return pd.DataFrame(results)

# Plotting
def plot_results(df):
    input_types = df["input_type"].unique()
    for input_type in input_types:
        sub_df = df[df["input_type"] == input_type]
        plt.plot(sub_df["size"], sub_df["randomized_time"], label=f"{input_type} (Randomized)", marker='o')
        plt.plot(sub_df["size"], sub_df["deterministic_time"], label=f"{input_type} (Deterministic)", marker='x')

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Randomized vs Deterministic Quicksort Performance")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("quicksort_comparison_plot.png")
    plt.show()

# Main
if __name__ == "__main__":
    sizes = [1000, 5000, 10000]
    df = run_comparisons_to_csv(sizes)
    plot_results(df)
