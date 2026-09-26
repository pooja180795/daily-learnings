# arr1 = [0,1,1,1]
# arr2 = [0,0,1,1]

# n = len(arr1)
# j = n
# carry = 0

# arr3 = [0] * (n+1)


# for i in range(n-1, -1, -1):
    
#     currSum = arr1[i] + arr2[i] + carry
#     print(currSum)
#     if currSum == 2:
#         arr3[j] = 0
#         j -= 1
#         carry = 1
#     elif currSum == 3:
#         arr3[j] = 1
#         j -= 1
#         carry = 1
#     else:
#         arr3[j] = currSum
#         j -= 1
#         carry = 0
# if carry == 1:
#     arr3[j] = carry 
# print(arr3)

# short version

arr1 = [1,0,1,1]
arr2 = [0,1,1,0]

n = len(arr1)
arr3 = [0] * (n+1)
carry = 0

for i in range(n-1,-1,-1):
    currSum = arr1[i] + arr2[i] + carry
    arr3[i+1] = currSum % 2
    carry = currSum // 2

arr3[0] = carry
print(arr3)