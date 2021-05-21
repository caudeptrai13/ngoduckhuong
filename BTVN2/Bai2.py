nums = [1,2,3,4,6]

def sum(nums):
    res = 0
    arr = []
    for i in range(len(nums)):
        res = res + nums[i]
        arr.append(res)
    return arr

print(sum(nums))