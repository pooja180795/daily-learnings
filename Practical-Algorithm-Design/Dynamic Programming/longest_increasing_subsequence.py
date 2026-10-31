# bottom-up approach, tc = O(n^2)

def lis(arr):
    n = len(arr)
    ans = [1] * (n)
    s = [-1] * n
    #print(len(ans))

    for i in range(n):
        for j in range(0, i):
            # if arr[j] < arr[i]:
            #     ans[i] = max(ans[i], ans[j] + 1)
            if (arr[j] < arr[i]) and (ans[j] + 1 > ans[i]):
                ans[i] = ans[j] + 1
                s[i] = j
    end = ans.index(max(ans))
    print_subsequence(arr, end, s)
    return max(ans)

def print_subsequence(arr,end,s):
    result = []
    while end != -1:
        result.append(arr[end])
        end = s[end]                # look here how end updated everytime :)
    result.reverse()
    print(result)


arr = [5,6,7,1,2,3,4,0,6]
#arr = [4,3,2,1]
print(lis(arr))

