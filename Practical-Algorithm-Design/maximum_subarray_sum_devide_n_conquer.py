# time complexiy = O(nlogn)

def findMidLen(arr):
    mid = len(arr) // 2
    sum = 0
    left_sum = float("-inf")
    right_sum = float("-inf")

    for i in range(mid, -1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum

    sum = 0
    for j in range(mid+1,len(arr)):
        sum += arr[j]
        if sum > right_sum:
            right_sum = sum

    return left_sum + right_sum


def ms_devide_n_con(arr):
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]

    left_len = ms_devide_n_con(L)
    right_len = ms_devide_n_con(R)

    mid_len = findMidLen(arr)

    return max(left_len,right_len, mid_len)


arr = [1,-7,4]
print(ms_devide_n_con(arr))