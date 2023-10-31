# "babad"
# "b" ->  "aba" -> "babad"
# -- odd number: l = i, r = i
# "ba" -> "abad"
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd number
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < r - l + 1:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even number
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < r - l + 1:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res
