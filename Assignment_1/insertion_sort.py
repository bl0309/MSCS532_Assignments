def insertion_sort_desc(arr):
    # Sorts an array in monotonically decreasing order using insertion sort.
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements that are less than key to one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def parse_input(input_str):
    # Parses a comma-separated string into a list of integers.
    # Example: "9,3,6,1" -> [9, 3, 6, 1]
    try:
        return [int(x.strip()) for x in input_str.split(',')]
    except ValueError:
        print("Error: Please enter a list of integers separated by commas.")
        return []


if __name__ == "__main__":
    print("Insertion Sort in Monotonically Decreasing Order")
    user_input = input("Enter a list of integers (comma-separated), or press Enter to use default: ")

    if user_input.strip():
        numbers = parse_input(user_input)
    else:
        print("\nNo user input numbers detected!")

        numbers = [7, 4, 8, 2, 22, 6]
        print("\nUsing default sample list:", numbers)

    if numbers:
        sorted_numbers = insertion_sort_desc(numbers)
        print("Sorted array (decreasing order):", sorted_numbers)