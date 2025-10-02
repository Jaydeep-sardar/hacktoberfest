def twoSum(nums, target):
    seen = {}  # number → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # if no solution
