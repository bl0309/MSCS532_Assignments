import random
import time
import tracemalloc
import pandas as pd
import matplotlib.pyplot as plt

# ─── Sorting Implementations ──────────────────────────────────────────────────

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid   = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result

# ─── Measurement Helpers ───────────────────────────────────────────────────────

def make_datasets(n):
    base = list(range(n))
    return {
        'sorted':  base[:],
        'reverse': base[::-1],
        'random':  random.sample(base, k=n)
    }

def measure(func, data):
    arr = data[:]  
    tracemalloc.start()
    t0 = time.perf_counter()
    func(arr)
    elapsed = time.perf_counter() - t0
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return elapsed, peak / 1024  # seconds, KB

# ─── Main Experiment ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    ns = [1000, 5000, 10000, 100000]
    results = []

    # run and collect
    for n in ns:
        datasets = make_datasets(n)
        for data_type, data in datasets.items():
            for name, algo in (('QuickSort', quick_sort), ('MergeSort', merge_sort)):
                t, m = measure(algo, data)
                results.append((name, n, data_type, t, m))
                print(f"{name:<10} {n:6} {data_type:>10} {t:10.4f} {m:10.1f}")

    # build DataFrame and save CSV
    df = pd.DataFrame(results, columns=["Algorithm","n","Type","Time_s","Mem_KB"])
    csv_path = "sort_performance_results.csv"
    df.to_csv(csv_path, index=False)
    print(f"\nResults saved to {csv_path}")

    # read back and plot
    df2 = pd.read_csv(csv_path)

    def plot_metric(df, metric, ylabel, title_prefix):
        for data_type in df["Type"].unique():
            subset = df[df["Type"] == data_type]
            plt.figure()
            for algo in df["Algorithm"].unique():
                sub = subset[subset["Algorithm"]==algo]
                plt.plot(sub["n"], sub[metric], label=algo)
            plt.title(f"{title_prefix} vs n ({data_type})")
            plt.xlabel("n (number of elements)")
            plt.ylabel(ylabel)
            plt.legend()
            plt.grid(True)
            plt.show()

    plot_metric(df2, "Time_s", "Time (seconds)", "Execution Time")
    plot_metric(df2, "Mem_KB", "Memory (KB)", "Memory Usage")
