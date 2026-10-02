def mergeSort(A):
    if len(A) < 2:
        return A
    mid = len(A) // 2
    L = A[:mid]
    R = A[mid:]
    L = mergeSort(L)
    R = mergeSort(R)
    i = j = 0
    C = []
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            C.append(L[i])
            i += 1
        else:
            C.append(R[j])
            j  += 1
    C += L[i:] + R[j:]
    return C

A = [5,3,2,4,1]
B = mergeSort(A)
print(B)
        