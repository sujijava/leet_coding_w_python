import pdb
from typing import List

# Input: amount = 5, coins = [1,2,5]
# Output: 4

from typing import List

class Solution:
    def change(self, amount, coins):
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        for c in range(len(coins) + 1):
            dp[c][0] = 1

        for a in range(1, amount + 1):
            for c in range(1, len(coins) + 1):
                without_new_coin = dp[c - 1][a]
                with_new_coin = 0
                new_coin = coins[c - 1]
                if a >= new_coin:
                    with_new_coin = dp[c][a - new_coin]
                dp[c][a] = with_new_coin + without_new_coin

        return dp[len(coins)][amount]

s = Solution()
amount = 5
coins = [1,2,5]
s.change(amount, coins)

'''Summary
- Best explanation: https://www.youtube.com/watch?v=DJ4a7cmjZY0&t=614s
- 
'''