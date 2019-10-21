def maximumProduct(nums):
    nums.sort()
    print(nums)
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

nums = [-4,5,8]
print(maximumProduct(nums))
# 128