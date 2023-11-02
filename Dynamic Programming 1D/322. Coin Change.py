from typing import List

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        # print(dp) # [0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]

        for a in range(1, amount + 1):
            for c in coins:
                # print(a) # 1 ~ 11 (inclusive)
                # print(c) # 1,2,5
                # a = 2
                # c = 2
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    # dp[2] = min(dp[2], 1 + dp[a-c])
        # print(dp) [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
        return dp[amount] if dp[amount] != amount + 1 else -1


s = Solution()
s.coinChange([1, 2, 5], 11)
