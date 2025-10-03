def recursive_binary_search(arr, low, high, key):
    if low > high:
        return -1
    mid=int((low+high)/2)
    if arr[mid] == key:
        return mid
    if arr[mid] > key:
        return recursive_binary_search(arr, low, mid-1, key)
    if arr[mid] < key:
        return recursive_binary_search(arr, mid+1, high, key)