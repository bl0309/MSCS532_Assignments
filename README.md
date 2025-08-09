# 1. MSCS532_Assignment_1

## Description
This repository contains a Python implementation of the Insertion Sort algorithm that sorts a list of numbers in **monotonically decreasing order**.

The project is part of the coursework for MSCS 532 and demonstrates understanding of algorithm implementation and version control using Git.

## Files
- `insertion_sort.py`: Contains the implementation of the insertion sort algorithm and a sample run.
- `README.md`: This file.

## How It Works
The algorithm iterates through the list and inserts each element into its correct position in a sorted (descending) portion of the list.

## Example

Input:  
[5, 2, 9, 1, 5, 6]

Output:  
[9, 6, 5, 5, 2, 1]
  
User Input:  
Insertion Sort in Monotonically Decreasing Order  
Enter a list of integers (comma-separated), or press Enter to use default:  
Using default list: [5, 2, 9, 1, 5, 6]  
Sorted array (decreasing): [9, 6, 5, 5, 2, 1]  


# 2. MSCS532_Assignment_2

## Sorting Implementations: 
Recursive in-place Quick Sort and Merge Sort.

## Performance Measurement: 
Uses time.perf_counter() for timing and tracemalloc for peak memory tracking.

## Datasets:

- Sorted (ascending)
- Reverse-sorted (descending)
- Random (uniformly shuffled)

## Data Export: 
Results saved as sort_performance_results.csv.

## Visualization: 
Plots execution time and memory usage vs. input size for each dataset type.

# 3. MSCS532_Assignment_3

## Run the script for Part 1: 
python3 quicksort_analysis.py

Output:
- quicksort_results.csv — contains raw timing data
- quicksort_comparison_plot.png — visual comparison of performance

## Run the script for Part 2: 
python3 has_table.py

Prints:
- A printed dictionary of key–value pairs after initial inserts.
- Correct search results.
- Confirmation of successful deletes.
- Automatic resizing once the load factor exceeds 0.75, doubling capacity and rehashing all entries.

# 4. MSCS532_Assignment_4

## Run the script for Part A: 
python3 heapsort.py

Output:
- A graph showing input size and execution time for the Heapsort algorithm.

## Run the script for Part B: 
python3 priority_queue.py

Output:
- A graph showing the result of Priority Queue Runtime vs Number of Tasks using a binary heap implementation.

# 5. MSCS532_Assignment_5

## Run the script: 
python3 randomize_sort.py

Output:
- A graph and summary performance tanle showing input size and execution time for the randomize algorithm (random, sorted and reverse).

# 6. MSCS532_Assignment_6

## Run the script for Part 1:
python3 selection_analysis.py

Output:
- A plotted graph of analysis of selection benchmark result and table result

## Run the script for Part 2:
python3 data_structure.py

Output:
- A plotted graph of analysis of data structure performance result and table result

# 7. MSCS532_Assignment_7

## Run the script:
python3 hash_table_insertion.py

Output:
- A plotted graph of analysis of selection benchmark result for Hash Table Insertion Time vs Load Factor

# 8. MSCS532_Final_Project

## Run the script:
python3 hpc_optimization.py

Output:
- A plotted graph of analysis of benchmark result for Performance, cache efficiency, and complexity analysis for naive, cache-optimized, and NumPy-based matrix multiplication implementations.