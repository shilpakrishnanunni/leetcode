# Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelset = ("aeiouAEIOU")
        output = []
        hashmap = {}
        place = []
        letters = []
        for i, letter in enumerate(s):
            if letter in vowelset:
                place.append(i)
                letters.append(letter)
        place.reverse()
        for i, j in zip(place, letters):
            hashmap[i] = j
        for i, letter in enumerate(s):
            if letter in vowelset:
                output.append(hashmap[i])
            else:
                output.append(letter)
        return "".join(output)

    def betterSolution(self, s: str) -> str:
        # “reverse selected elements” problem.
        # This pattern appears in:
            # Reverse string
            # Valid palindrome
            # Move zeroes
            # Remove element
            # Partition problems
        vowels = set("aeiouAEIOU")
        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)

print(Solution().reverseVowels("IceCreAm")) # "AceCreIm"
