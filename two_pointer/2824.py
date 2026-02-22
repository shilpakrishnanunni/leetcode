# Count Pairs Whose Sum is Less than Target
# Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
from typing import List
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pairs = 0
        hashmap = {}
        for i in nums:
            max_j = target - i
            # hashmap.get()


        return pairs

print(Solution().countPairs(nums = [-1,1,2,3,1], target = 2)) # 3
# print(Solution().countPairs(nums = [-6,2,5,-2,-7,-1,3], target = -2)) # 10
