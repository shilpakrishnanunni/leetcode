# Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        height_len = len(height)
        left = 0
        right = height_len - 1
        max_area = 0
        while left < right:
            print("left right", left, right)
            new_area = min(height[left], height[right]) * (right - left)
            print(f"{new_area} = {height[left], height[right]} * {(right - left)}")
            max_area = max(new_area, max_area)
            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1
            
        return max_area

print(Solution().maxArea([1,8,6,2,5,4,8,3,7])) # 49
