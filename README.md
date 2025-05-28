# MSCS532_Assignment1

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


# MSCS532_Assignment2

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