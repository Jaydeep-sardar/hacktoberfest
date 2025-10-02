# Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0 . The solution must not contain duplicate triplets (e.g., [1, 2, 3] and [2, 3, 1] are considered duplicates). If no such triplets are found, return an empty array.

# Each triplet can be arranged in any order, and the output can be returned in any order.

# Example:
# Input: nums = [0, -1, 2, -3, 1]
# Output: [[-3, 1, 2], [-1, 0, 1]]


from typing import List

def triplet_sum(nums: List[int]) -> List[List[int]]:
    # Write your code here
    nums.sort()  # Step 1: Sort the array
    res = []
    n = len(nums)

    for i in range(n - 2):
        # Skip duplicate elements for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                # Skip duplicates for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return res
