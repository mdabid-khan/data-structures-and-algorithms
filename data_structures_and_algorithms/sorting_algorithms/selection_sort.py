def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [7, 4, -23, 97, 1]
print(f"Before sorting: {arr}")

selection_sort(arr)
print(f"After sorting: {arr}")