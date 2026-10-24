k = 0
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
    
    global k
    # abhis loop:)
    while i < len(L)+1  and j < len(R)+1:
        k += 1
        
        if i== len(L) and j == len(R):
            k -= 1
            break
        elif i < len(L) and j < len(R):
                    if L[i] <= R[j]:
                        C.append(L[i])
                        i += 1
                    else:
                        C.append(R[j])
                        j += 1
        elif i == len(L):
            C.append(R[j])
            j += 1
        elif j == len(R):
            C.append(L[i])
            i += 1
            
    # while i < len(L):
    #     C.append(L[i])
    #     i += 1

    # while j < len(R):
    #     C.append(R[j])
    #     j += 1

    #C += L[i:]+ R[j:]

    return C

# 5 arr = [4,1,3,2]  
# 5 arr = [1,4,3,2]
arr = [2,1,5,3,8,9,7,6]
ans = mSort(arr)

print(ans)
print(k)

    