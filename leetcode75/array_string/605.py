# Can Place Flowers
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed_len = len(flowerbed)
        count = 0
        flower_planted_last_loop = False
        for i in range(flowerbed_len):
            if flowerbed[i]:
                flower_planted_last_loop = False
                continue
            if i == 0:
                print("i", i, "flowerbed[i]", flowerbed[i], "flowerbed[i+1]", flowerbed[i+1])
                if flowerbed[i] == 0:
                    if flowerbed_len == 1 or flowerbed[i+1] == 0:
                        count += 1
                        flower_planted_last_loop = True
                        print("count", count, "flower_planted_last_loop", flower_planted_last_loop)
                        continue
                else:
                    flower_planted_last_loop = False
                    continue
            if i == flowerbed_len - 1:
                print("i", i, "flowerbed[i]", flowerbed[i], "flowerbed[i-1]", flowerbed[i-1])
                if flowerbed[i-1] or flowerbed[i]:
                    flower_planted_last_loop = False
                    continue
                if not flower_planted_last_loop:
                    count +=1
                    flower_planted_last_loop = True
                    print("count", count, "flower_planted_last_loop", flower_planted_last_loop)
                continue

            print("i", i, "flowerbed[i-1]", flowerbed[i-1], "flowerbed[i+1]", flowerbed[i+1])
            if flowerbed[i-1] or flowerbed[i+1]:
                flower_planted_last_loop = False
                continue
            if not flower_planted_last_loop:
                count += 1
                flower_planted_last_loop = True
                print("count", count, "flower_planted_last_loop", flower_planted_last_loop)
                continue
            flower_planted_last_loop = False
        return count >= n
    
    def betterSolution(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                left = (i == 0) or (flowerbed[i - 1] == 0)
                right = (i == length - 1) or (flowerbed[i + 1] == 0)

                if left and right:
                    flowerbed[i] = 1
                    count += 1

        return count >= n


# print(Solution().canPlaceFlowers([1,0,0,0,1], 1)) # True
# print(Solution().canPlaceFlowers([1,0,0,0,1], 2)) # False
# print(Solution().canPlaceFlowers([1,0,0,0,0,0,1], 2)) # True
print(Solution().canPlaceFlowers([1,0,0,0,0,1], 2)) # False
# print(Solution().canPlaceFlowers([1,0,1,0,1,0,1], 0)) # False
