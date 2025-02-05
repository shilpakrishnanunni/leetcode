class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        '''
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


    def isPalindrome(self, x: int) -> bool:
        '''
        Given an integer x, return true if x is a palindrome, and false otherwise.
        '''
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        num = list(str(x))
        palindrome = "".join(num[::-1])
        return bool(str(x) == palindrome)


    def removeDuplicates(self, nums: list[int]) -> int:
        '''
        Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
        '''
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
    

    def removeElement(self, nums: list[int], val: int) -> int:
        '''
        Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
        '''
        j = 1
        for i in range(1, len(nums)):
            if nums[i] == val:
                nums[i] = nums[i-1]
        return nums


    def searchInsert(self, nums: list[int], target: int) -> int:
        '''
        Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.
        '''
        # TODO
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)


    def lengthOfLastWord(self, s: str) -> int:
        '''
        Given a string s consisting of words and spaces, return the length of the last word in the string.
        '''
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


    def longestCommonPrefix(self, strs: list[str]) -> str:
        '''
        Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
        '''
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


    def plusOne(self, digits: list[int]) -> list[int]:
        '''
        You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's. Increment the large integer by one and return the resulting array of digits.
        '''
        # digits.reverse() # O(n)
        # result = []
        # carry = 0

        # for i, num in enumerate(digits): # O(n)
        #     if i == 0:
        #         if num == 9:
        #             result.append(0)
        #             carry = 1
        #             if i == len(digits) - 1:
        #                 result.append(1)
        #         else:
        #             result.append(num + 1)
        #     elif num == 9 and carry == 1:
        #         result.append(0)
        #         if i == len(digits) - 1:
        #             result.append(1)
        #     else:
        #         result.append(num + carry)
        #         carry = 0
        # result.reverse() # O(n)
        # return result

        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


    def isArraySpecial(self, nums: list[int]) -> bool:
        '''
        An array is considered special if every pair of its adjacent elements contains two numbers with different parity. You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.
        '''
        if len(nums) == 1:
            return True
        for i in range(0, len(nums)-1):
            # print(f"{nums[i]} % 2",nums[i] % 2,f"{nums[i+1]} % 2",nums[i+1] % 2)
            if (nums[i] % 2) == (nums[i+1] % 2):
                return False
        return True
            
        
    def checkRotatedArray(self, nums: list[int]) -> bool:
        '''
        Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

        There may be duplicates in the original array.

        Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
        '''
        # def degree_of_rotation(arr):
        #     for i in range(0, len(arr)):
        #         if arr[i] < arr[i-1]:
        #             if arr[i] < arr[0]:
        #                 return i
        # org_nums = nums[:]
        # rot = degree_of_rotation(org_nums)
        # if not rot:
        #     rot = 0
        # nums.sort()
        # length = len(nums)
        # for i in range(length):
        #     if nums[i] != org_nums[(i+rot) % length]:
        #         return False

        # return True
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
            if count > 1:
                return False
        return True


    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        '''
        You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.
        '''
        n = len(nums)
        inc = 1
        dec = 1
        longest = 1

        for i in range(1,n):
            print(nums[i-1], nums[i],)
            if nums[i] > nums[i-1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i-1]:
                dec += 1
                inc = 1
            elif nums[i] == nums[i-1]:
                inc = 1
                dec = 1
            print(f"inc {inc} dec {dec}")
            longest = max(longest, inc, dec)
        return longest
        
    
    def maxAscendingSum(self, nums: list[int]) -> int:
        '''
        Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

        A subarray is defined as a contiguous sequence of numbers in an array.

        A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.
        '''
        n = len(nums)
        largest_sum = nums[0]
        sum = nums[0]
        for i in range(1,n):
            if nums[i] <= nums[i-1]:
                sum = nums[i]
            else:
                sum += nums[i]
            largest_sum = max(largest_sum, sum)
            # print(f"nums[i] {nums[i]} sum {sum} largest_sum {largest_sum}")
        return largest_sum


    def isValid(self, s: str) -> bool:
        '''
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

        An input string is valid if:

        1) Open brackets must be closed by the same type of brackets.

        2) Open brackets must be closed in the correct order.

        3) Every close bracket has a corresponding open bracket of the same type.

        '''
        if len(s) % 2 != 0:
            return False
        flag_order_arr = []
        my_hash = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for i in s:
            if i in ["(", "{", "["]:
                flag_order_arr.append(i)
            if i in [")", "}", "]"]:
                if len(flag_order_arr) > 0 and flag_order_arr[-1] == my_hash[i]:
                    flag_order_arr.pop()
                else:
                    return False
        if len(flag_order_arr) > 0:
            return False
        return True


    def strStr(self, haystack: str, needle: str) -> int:
        '''
        Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
        '''
        m, n = len(needle), len(haystack)
        if m == 0:
            return 0
        if m > n:
            return -1

        # for i in range(n - m + 1):
        #     # j = 0
        #     # while j < len(needle) and haystack[i+j] == needle[j]:
        #     #     j+=1
        #     # if j == len(needle):
        #     #     return i
        #     if haystack[i:i+m] == needle:
        #         return i
        # return -1

        ## KMP algorithm O(n+m)
        lps = [0] * m
        j = 0
        # Preprocess the pattern to build the LPS table
        for i in range(1, m):
            # print(needle[i], needle[j])
            while j > 0 and needle[i] != needle[j]:
                j = lps[j - 1]
            if needle[i] == needle[j]:
                j += 1
            lps[i] = j
            # print(f"j {j} lps {lps}")
        print(lps)

        # Perform the search
        j = 0
        for i in range(n):
            while j > 0 and haystack[i] != needle[j]:
                j = lps[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == m:
                return i - m + 1

        return -1


    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        '''
        You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

        Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.
        '''
        not_equal_count = 0
        n = len(s1)
        my_hash = {}
        for i in range(n):
            print(f"s1[i] {s1[i]}")
            if s1[i] not in s2:
                return False
            if s2[i] != s1[i]:
                not_equal_count += 1
                if not_equal_count > 2:
                    return False
                my_hash[s2[i]] = i
                print("temp hash ",my_hash)
                if not_equal_count == 2:
                    print("check switch", s1[i], my_hash)
                    if s1[i] not in my_hash:
                        return False
                    print(f"my_hash[{s2[i]}] {my_hash[s2[i]]} i {i}")
                    if my_hash[s2[i]] != i:
                        print("uh oh")
                        return False
        if len(my_hash) % 2 != 0:
            return False
        print("final hash",my_hash)
        return True




# print(Solution().areAlmostEqual("bank", "kanb"))
print(Solution().areAlmostEqual("bankb", "kannb"))
# print(Solution().areAlmostEqual("akrjnhuojtkhlqdfifwxbsmphhcchuqcconcvplcyxjpi", "akrjnhuojtkhlxdfifwqbsmphhcchuqcconcvplcyxjpi"))
# print(Solution().strStr("ababcabcabababd", "ababd"))
# print(Solution().isValid("){"))
# print(Solution().maxAscendingSum([10,20,30,5,10,50]))
# print(Solution().longestMonotonicSubarray([1,4,5,3,3,2]))
# print(Solution().checkRotatedArray([6,10,6]))
# print(Solution().isArraySpecial([2,1,4]))
# print(Solution().plusOne([9, 9]))
# print(Solution().longestCommonPrefix(["flower","flow","flight"]))
# print("result",Solution().twoSum([2,7,11,15], 9))
# print(Solution().isPalindrome(0))
# print(Solution().removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))
# print(Solution().removeElement([0,1,2,2,3,0,4,2], 3))
# print(Solution().searchInsert([1,3,5,6], 5))
# print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
