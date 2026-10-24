# time compplexity(best case) = O(nlogn)

def quickSort(arr, st, end):
    if st < end:
        pivot = partition(arr, st, end)
        left = quickSort(arr, st, pivot-1)
        right = quickSort(arr, pivot+1, end)


def partition(arr, st, end):
    i = st-1
    pivot = arr[end]

    for j in range(st, end):
        if arr[j] < pivot:
            i += 1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
    i += 1
    temp = arr[end]
    
    arr[end] = arr[i]
    arr[i] = temp
    return i


arr = [4,3,7,1,22,8,4,9]
quickSort(arr, 0, len(arr)-1)
print(arr)