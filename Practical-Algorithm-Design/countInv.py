def ms(arr):
    if len(arr) < 2:
        return arr,0
    mid = len(arr) // 2
    lArr = arr[:mid]
    rArr = arr[mid:]
    lArr, linv = ms(lArr)
    rArr, rinv = ms(rArr)

    i = j = 0
    ans = []
    inv = 0
    while i < len(lArr) and j < len(rArr):
        if lArr[i] <= rArr[j]:
            ans.append(lArr[i])
            i += 1
        else:
            ans.append(rArr[j])
            inv += len(lArr)-i
            j += 1

    ans += lArr[i:] + rArr[j:]

    print(ans)
    print(linv +rinv+inv)
    return ans, linv +rinv+inv
    

arr = [4,6,1,5,2,3]
ms(arr)