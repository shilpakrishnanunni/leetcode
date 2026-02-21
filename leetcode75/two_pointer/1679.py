# Max Number of K-Sum Pairs
# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.
from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        while len(nums) > 1:
            ...



print(Solution().maxOperations(nums = [1,2,3,4], k = 5)) # 2
