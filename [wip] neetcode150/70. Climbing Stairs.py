class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[1] = 1
        memo[2] = 2

        def helper(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = helper(n-1) + helper(n-2)
                return memo[n]

        return helper

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        dp[1] = 1
        dp[2] = 2

        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev = 2
        prevPrev = 1
        res = 3

        for i in range(3,n+1):
            res = prev + prevPrev # 3
            temp = prev # 1
            prev = res # 3
            prevPrev = temp #

        return res
