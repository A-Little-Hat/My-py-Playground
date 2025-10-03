def ordered_sequential_search(arr, key):
    sorted(arr)
    for i in range(len(arr)):
        if arr[i] > key:
            return -1
        if arr[i] == key:
            return i
    return -1