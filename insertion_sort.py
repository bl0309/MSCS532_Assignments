def insertion_sort_desc(arr):
    """
    Sorts an array in monotonically decreasing order using insertion sort.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements that are less than key to one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    sample = [7, 4, 8, 2, 22, 6]
    print("Original array:", sample)
    sorted_sample = insertion_sort_desc(sample)
    print("Sorted array (decreasing order):", sorted_sample)