function bubbleSort(arr):
    n = length(arr)
    for i from 0 to n - 1:
        # Flag to optimize the algorithm by detecting if any swap happened in this iteration
        swapped = False
        for j from 0 to n - i - 1:
            if arr[j] > arr[j + 1]:
                # Swap if the current element is greater than the next one
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped in the inner loop, then the array is already sorted
        if not swapped:
            break
    return arr


function quickSort(arr):
    if length(arr) <= 1:
        return arr
    else:
        # Select a pivot element
        pivot = arr[0]
        # Partition the array around the pivot
        left = [elements in arr less than pivot]
        right = [elements in arr greater than pivot]
        # Recursively apply quicksort to the left and right partitions
        return quickSort(left) + [pivot] + quickSort(right)
