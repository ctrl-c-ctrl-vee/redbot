def quicksort(arr):
    # Base case: if the array is empty or has one element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot (here we use the last element)
    pivot = arr[-1]
    
    # Partition the array into three parts:
    # elements less than the pivot, elements equal to the pivot, and elements greater than the pivot
    smaller, equal, larger = [], [], []
    for num in arr:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)
    
    # Recursively sort the smaller and larger parts
    return quicksort(smaller) + equal + quicksort(larger)

# Example usage
if __name__ == "__main__":
    test_array = [3, 6, 8, 10, 1, 2, 1]
    print("Original array:", test_array)
    sorted_array = quicksort(test_array)
    print("Sorted array:", sorted_array)
