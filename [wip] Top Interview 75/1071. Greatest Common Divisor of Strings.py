# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            divisor = min(len(str1), len(str2))
            while divisor > 0:
                if len(str1) % divisor == 0 and len(str2) % divisor == 0:
                    break
                divisor -= 1
            return str1[:divisor]
        else:
            return ""


'''
Summary:

Complexity:
 - Time: O(N) N is min(len(str1), len(str2))
 - Space: O(1)
'''
