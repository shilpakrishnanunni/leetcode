# Is Subsequence
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        slow = 0
        for fast in t:
            print(fast)
            if slow < len(s) and fast == s[slow]:
                slow += 1
        print(f"slow {slow} len(s) {len(s)}")
        return slow == len(s)

print(Solution().isSubsequence("abc", "ahbgdc")) # true
print(Solution().isSubsequence("", "ahbgdc")) # true
print(Solution().isSubsequence("b", "abc")) # true
