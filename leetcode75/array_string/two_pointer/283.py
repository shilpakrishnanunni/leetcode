# Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        slow = 0
        for fast in range(nums_len):
            # print(fast, nums[fast])
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        # print("new nums", nums, "slow", slow)
        for i in range(slow, nums_len):
            nums[i] = 0
    
print(Solution().moveZeroes([0,1,0,3,12])) # [1,3,12,0,0]
# print(Solution().moveZeroes([0,0,1])) # [1,0,0]
