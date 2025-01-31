class Solution:

    # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # for i, num in enumerate(nums):
        #     for j in range(i + 1, len(nums)):
        #         if target - num == nums[j]:
        #             return [i, j]

        # indexed_nums = [(num, i) for i, num in enumerate(nums)  ]
        # # print(indexed_nums)
        # indexed_nums.sort(key=lambda x: x[0])
        # # print(indexed_nums)

        # left, right = 0, len(indexed_nums) - 1
        # while left < right:
        #     current_sum = indexed_nums[left][0] + indexed_nums[right][0]
        #     if current_sum == target:
        #         return [indexed_nums[left][1], indexed_nums[right][1]]
        #     elif current_sum < target:
        #         left += 1
        #     else:
        #         right -=1
        nums.reverse()
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
            print(num_map)
        return []

    # Given an integer x, return true if x is a palindrome, and false otherwise.
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        num = list(str(x))
        palindrome = "".join(num[::-1])
        return bool(str(x) == palindrome)

    # Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
    def removeDuplicates(self, nums: list[int]) -> int:
        # my_set = set(nums)
        # k = len(my_set)
        # print(my_set, k)
        # nums = list(my_set)
        # return k, nums
        j = 1
        for i in range(1, len(nums)):
            if nums[i] !=  nums[i-1]:
                nums[j] = nums[i]
                j +=1
        return j, nums
    
    # Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
    def removeElement(self, nums: list[int], val: int) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] == val:
                nums[i] = nums[i-1]
        return nums
    
    # Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        lps = []
        # for i in range(0, len(haystack)):
            # if 

    # Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)

    # Given a string s consisting of words and spaces, return the length of the last word in the string.
    def lengthOfLastWord(self, s: str) -> int:
        # split_str = [word for word in s.split(" ") if word is not ""]
        # return len(split_str[-1])

        length = 0
        i = len(s) - 1

        while i >= 0 and s[i] == ' ':
            i -= 1

        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length

    # Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # if len(strs) == 1:
        #     return strs[0]

        # strs.sort()
        # longest_prefix = []
        # first, last = strs[0], strs[-1]

        # if not first or not last or first[0] != last [0]:
        #     return ""

        # for i, letter in enumerate(first):
        #     if last[i] and last[i] == letter:
        #         longest_prefix.append(letter)
        #     else:
        #         break

        # return "".join(longest_prefix)
        if not strs:
            return ""
        
        prefix = strs[0]

        for string in strs[1:]:

            while string.startswith(prefix):
                prefix=prefix[:-1]
                if not prefix:
                    return ""
        return prefix



print(Solution().longestCommonPrefix(["flower","flow","flight"]))
# print("result",Solution().twoSum([2,7,11,15], 9))
# print(Solution().isPalindrome(0))
# print(Solution().removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))
# print(Solution().removeElement([0,1,2,2,3,0,4,2], 3))
# print(Solution().strStr("sabutsad", "sad"))
# print(Solution().searchInsert([1,3,5,6], 5))
# print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
