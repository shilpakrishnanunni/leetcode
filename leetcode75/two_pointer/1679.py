# Max Number of K-Sum Pairs
# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.
from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ops = 0
        left = 0
        right = len(nums) - 1
        print(nums)
        while left < right:
            print(left, right)
            sum = nums[left] + nums[right]
            if sum == k:
                ops += 1
                left += 1
                right -= 1
            elif sum < k:
                left +=1
            else:
                right -= 1

        return ops
    
    def betterSolution(self, nums: List[int], k: int) -> int:
        # hashmap solution
        ops = 0
        hashmap = {}
        for i in nums:
            j = k - i
            if hashmap.get(j, 0) > 0:
                ops += 1
                hashmap[j] -= 1
            else:
                hashmap[i] = hashmap.get(i, 0) + 1
            print(hashmap)

        return ops




# print(Solution().maxOperations(nums = [1,2,3,4], k = 5)) # 2
# print(Solution().betterSolution(nums = [3,1,3,4,3], k = 6)) # 1
print(Solution().betterSolution(nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], k = 2)) # 2
