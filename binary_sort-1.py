def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target value.

    :param arr: List[int] - A sorted list of integers.
    :param target: int - The integer value to search for.
    :return: int - The index of the target if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 7
result = binary_search(sorted_array, target_value)
print(f"Index of {target_value} is: {result}")
