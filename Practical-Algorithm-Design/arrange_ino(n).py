nums = [-5,-3,5,-9,3,-7,5,7]

i = 0
j = len(nums)-1

while i<j:
    while i<j and nums[i] < 0:
        i += 1
    while i<j and nums[j] >= 0:
        j -= 1
    if i < j:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i += 1
        j -= 1
print(nums)
