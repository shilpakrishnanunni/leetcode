# 1768. Merge Strings Alternately
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Time: O(n + m)
        # Space: O(n + m)
        output = []
        n1, n2 = len(word1), len(word2)
        for i in range(max(n1, n2)):
            if i < n1:
                output.append(word1[i])
            if i < n2:
                output.append(word2[i])
        return "".join(output)

    def betterSolution(self, word1: str, word2: str) -> str:
        result = []
        for c1, c2 in zip(word1, word2):
            result.append(c1)
            result.append(c2)
        return "".join(result) + word1[len(word2):] + word2[len(word1):]


# print(Solution().mergeAlternately("abc", "pqr"))  # "apbqcr"
# print(Solution().mergeAlternately("ab", "pqrs"))  # "apbqrs"
print(Solution().mergeAlternately("abcd", "pq"))  # "apbqcd"
