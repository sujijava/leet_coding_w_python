# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1): # 0 ~ 7 inclusive
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    # s[4:8] -> "code"
                    # s[0:4] -> "leet"
                    dp[i] = dp[i + len(w)]
                if dp[i]: 
                    break
        # print(dp)
        return dp[0]
s = Solution()

# string = "applepenapple"
# wordDict = ["apple", "pen"]

# string = "leetcode"
# wordDict = ["leet", "code"]

string = "abcd"
wordDict = ["a","abc","b","cd"]

s.wordBreak(string, wordDict)

'''Summary
if dp[i]: break ???????????/
Why does it needed???? 
'''