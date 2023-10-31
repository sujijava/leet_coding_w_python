# input: "1023"
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        for i in range(len(s) - 1, -1, -1):
            print(i) # 3,2,1,0
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]

        return dp[0]

s = Solution()
s.numDecodings("1023")

# input: "1023"

# dp[3] = 1 represents the number of ways to decode the substring "3."
# dp[2] = 2 represents the number of ways to decode the substring "23."
# dp[1] = 0 represents the number of ways to decode the substring "023."
# dp[0] = 2 represents the number of ways to decode the entire input string "1023."
