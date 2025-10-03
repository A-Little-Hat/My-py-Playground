def iterative_binary_search(arr, key):
    sorted(arr)
    low=0
    high=len(arr)
    mid=int(high/2)
    while low <= high:
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            high=mid-1
        if arr[mid] < key:
            low=mid+1
        mid=int((low+high)/2)
    return -1