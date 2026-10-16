def ms(arr):
    maxSum = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum += arr[j]
            if sum > maxSum:
                maxSum = sum

    return maxSum

arr = [1,-2,4,0,2,-1,3,-1]
sum = ms(arr)
print(sum)