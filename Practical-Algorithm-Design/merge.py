def mSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2

    L = arr[:mid]
    R = arr[mid:]

    L = mSort(L)
    R = mSort(R)
    C = []

    i = j = 0

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            C.append(L[i])
            i += 1
        else:
            C.append(R[j])
            j += 1
    # while i < len(L):
    #     C.append(L[i])
    #     i += 1

    # while j < len(R):
    #     C.append(R[j])
    #     j += 1

    C += L[i:]+ R[j:]

    return C

arr = [4,3,9,2,1,6]
ans = mSort(arr)
print(ans)

    