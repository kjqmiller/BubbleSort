# Bubble sort algorithm, compares values of neighboring indices and swaps them if they are out of order
# After each pass the array will have i elements sorted
arr = [54, 777, 1, 2, 44.44, 17, 17, 44455, 23, -17, 0]
print(f'Unsorted array: {arr}')

length = len(arr)

# Traverse all unsorted items, larger values are "bubbled" to the right of the array as the inner loop compares indices
# Outer loop tracks how many values have been sorted so inner loop does not compare already sorted values
for i in range(length):
    for ii in range(0, length - i - 1):
        # If current index is greater than next, swap them
        if arr[ii] > arr[ii + 1]:
            arr[ii], arr[ii + 1] = arr[ii + 1], arr[ii]

# Print the original array again as proof that it was sorted
print(f'Sorted array: {arr}')
