arr = [2,25,1,33,14]
#arr = [1,2,3,4,5]

for i in range(len(arr)):
    min = arr[i]
    index = i
    for j in range(i+1, len(arr)):
        if arr[j] < min:
            min = arr[j]
            index = j
    temp = arr[i]
    arr[i] = arr[index]
    arr[index] = temp

print(arr)
print("worst case = best case = Big theta(n^2)")
