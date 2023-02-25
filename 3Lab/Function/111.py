def ff(nums, p):
    if len(nums)==0:
        return p
    p+=nums[len(nums)-1]
    nums.pop()
    return ff(nums, p)
print(ff([1,2,3], 0))