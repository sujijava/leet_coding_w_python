# Input: cost = [10,15,20]
# Output: 15

'''Summary
 Recurrence Relation:
 - mincost(i) = cost[i]+min(mincost(i-1), mincost(i-2))
 Base cases:
 - mincost(0) = cost[0]
 - mincost(1) = cost[1]
'''

# DP
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         length = len(cost)
#         dp = [0] * length
#         dp[0] = cost[0]
#         dp[1] = cost[1]

#         for i in range(2,length): #2
#             dp[i] = cost[i] + min(dp[i -1], dp[i-2])

#         return min(dp[length -1], dp[length-2])

# Recursion + memo = 0

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        self.memo = {}
        self.memo[0] = cost[0]
        self.memo[1] = cost[1]
        length = len(cost)
        return min(self.helper(length-1), self.helper(length-2))

    def helper(self, n):
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.cost[n] + min(self.helper(n-1), self.helper(n-2))
        return self.memo[n]
