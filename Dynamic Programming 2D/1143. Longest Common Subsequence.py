class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROW = len(text1) 
        COL = len(text2)

        dp = [[0] * (COL + 1) for _ in range(ROW + 1)]

        for r in range(ROW -1, -1, -1):
            for c in range(COL -1, -1, -1):
                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r][c+1], dp[r+1][c])

        return dp[0][0]

# Input: text1 = "abcde", text2 = "ace"
s = Solution()
s.longestCommonSubsequence("abcde", "ace")

''''
   [ a  c  e
a   [0, 0, 0, 0],
b   [0, 0, 0, 0],
c   [0, 0, 0, 0],
d   [0, 0, 0, 0],
e   [0, 0, 0, 0],
    [0, 0, 0, 0]]

  [  a  c  e
a   [0, 0, 0, 0],
b   [0, 0, 0, 0],
c   [0, 0, 0, 0],
d   [0, 0, 0, 0],
e   [0, 0, 1, 0]],

  [  a  c  e
a   [0, 0, 0, 0],
b   [0, 0, 0, 0],
c   [0, 2, 1, 0],
d   [1, 1, 1, 0],
e   [1, 1, 1, 0]],


   [ a  c  e
a   [3, 2, 1, 0],
b   [2, 2, 1, 0],
c   [2, 2, 1, 0],
d   [1, 1, 1, 0],
e   [1, 1, 1, 0]],

Other examples
"abc", "abc" 
   [  a  b  c
a    [3, 2, 1, 0],
b    [2, 2, 1, 0],
c    [1, 1, 1, 0],
     [0, 0, 0, 0]]

*** understanding ELSE block ***

else:
    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])


When characters text1[i] and text2[j] don't match, 
it means they can't both be part of the same common subsequence (LCS).

You have two options:
Exclude text1[i] 
- and find the LCS of the remaining part of text1 with text2.
Exclude text2[j] 
- and find the LCS of text1 with the remaining part of text2.

dp[i][j] = max(dp[i][j + 1], dp[i + 1][j]) compares these two options and selects the one that results in the longer LCS. This way, it ensures the LCS calculation considers both characters' exclusion and picks the path with the maximum length.

'''
