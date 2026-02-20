# 1071. Greatest Common Divisor of Strings
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
# Hint: The greatest common divisor must be a prefix of each string, so we can try all prefixes.
# Constraints: 1 <= str1.length, str2.length <= 1000

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        sol = ""
        n1, n2 = len(str1), len(str2)
        if n1 == n2:
            if str1 == str2:
                return str1
            return sol

        if n1 < n2:
            small = str1
            big = str2
        else:
            small = str2
            big = str1
        print(f"big {big} small {small}")
        len_small = len(small)
        len_big = len(big)
        compare = small
        len_compare = len(compare)
        flag = True
        while len_compare > 0:
            print("start while. compare:", compare)
            if len_big % len_compare != 0:
                print("len big", len_big, "not divisible by len compare", len_compare)
                compare = compare[:-1]
                len_compare = len(compare)
                continue
            if len_small % len_compare != 0:
                print("len small", len_small, "not divisible by len compare", len_compare)
                compare = compare[:-1]
                len_compare = len(compare)
                continue
            diff = len_compare
            x = 0
            y = diff
            print("diff", diff, "compare", compare)
            while y <= len_big:
                print("inside mini while. y", y, "big[x:y]", big[x:y])
                if big[x:y] != compare:
                    print("chunk of big", big[x:y], "compare", compare)
                    flag = False
                    break
                if y <= len_small:
                    if small[x:y] != compare:
                        print("chunk of small", small[x:y], "compare", compare)
                        flag = False
                        break
                print("chunk of big", big[x:y], "compare", compare, "-> good")
                flag = True
                x += diff
                y += diff
            if flag:
                sol = compare
                print("found solution", sol)
                break
            compare = compare[:-1]
            len_compare = len(compare)
            print("new compare", compare)
        return sol

    def betterSolution(self, str1: str, str2: str) -> str:
        import math
        if str1 + str2 != str2 + str1:
            return ""
        gcd_len = math.gcd(len(str1), len(str2))
        return str1[:gcd_len]




# print(Solution().gcdOfStrings("ABCABC", "ABC"))  # "ABC"
# print(Solution().gcdOfStrings("ABABAB", "ABAB"))  # "AB"
# print(Solution().gcdOfStrings("LEET", "CODE"))  # ""
# print(Solution().gcdOfStrings("AAAAAB", "AAA"))  # ""
print(Solution().betterSolution("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")) # "TAUXX"
# print(Solution().betterSolution("AAAAAAAAA", "AAACCC")) # ""
