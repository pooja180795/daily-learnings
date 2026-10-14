def binSearch(arr, st, end, key):
    if st > end:
        return -1
    mid = st + (end-st)//2
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binSearch(arr, mid+1, end, key)
    else:
        return binSearch(arr, st, mid-1, key)

arr = [2,5,7,8,10,12,14]
key = 10
index = binSearch(arr, 0, len(arr) - 1, key)
print(index)
