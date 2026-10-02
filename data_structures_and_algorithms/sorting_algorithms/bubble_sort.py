def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = [1, 2, 7, 5, -1, 3, 2]
print(f"Before sorting: {arr}")

bubble_sort(arr)
print(f"After sorting: {arr}")