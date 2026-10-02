def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        current_number = arr[i]
        position = i

        while position > 0 and arr[position - 1] > current_number:
            arr[position] = arr[position - 1]
            position = position - 1

        arr[position] = current_number

    return arr


arr = [7, 4, -23, 97, 1, 67, 6, -23]
print(f"Before sorting: {arr}")

insertion_sort(arr)
print(f"After sorting: {arr}")