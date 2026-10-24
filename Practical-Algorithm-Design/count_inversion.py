# time complexity = mergesort complexity = 2T(n/2) + O(n) = O(nlogn)

def countInversion(arr):
    if len(arr) < 2:
        return arr, 0

    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]

    L, l_inv = countInversion(L)            # count of left inversion
    R, r_inv = countInversion(R)            # count of right inversion

    i = j = 0
    C = []
    inv = 0                                 # count of left and right between inversion
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            C.append(L[i])
            i += 1
        else: 
            if L[i] > R[j] * 2:
                C.append(R[j])
                inv += len(L[i:])
                j += 1
            else:
                C.append(R[j])
                j += 1

    
    C += L[i:] + R[j:]


    print(C)
    print(inv+l_inv+r_inv)
    return C, inv + l_inv + r_inv

arr = [4,6,1,5,2,3]
countInversion(arr)


