# for insertion sort best case time complexity = big theta(n)
# worst case time complexity = big theta(n^2)  = average case tc

arr = [5,6,3,22,1]

for i in range(1,len(arr)):
    curr = arr[i]
    j = i
    while j > 0 and arr[j-1] > curr:
        arr[j] = arr[j-1]
        j -= 1
    arr[j] = curr

print(arr)