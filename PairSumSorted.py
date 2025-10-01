from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    
    while left < right:
        s = nums[left] + nums[right]
        
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    
    return []
