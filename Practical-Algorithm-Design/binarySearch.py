
def binarySearch(arr, key, left, right):
    if right < left:
        return -1
    if left == right:
        if arr[left] == key:
            return left
        else:
            return -1
    mid = left + (right-left)//2
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binarySearch(arr, key, mid+1, right)
    else:
        return binarySearch(arr, key, left, mid-1)

arr = [5,55,89,90,678]
n = len(arr)
print(n)
print(binarySearch(arr, 5, 0, n-1))