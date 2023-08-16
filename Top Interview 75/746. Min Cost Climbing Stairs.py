class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        curr = min(cost[0], cost[1])
        cost = 0

        while curr < len(cost) - 1:
            if curr == 0:
                cur_num = min(cost[0], cost[1
                                            else:
                                            cur_num=cost[curr]
                                            n_num=cost[curr+1]
                                            n_n_num=cost[curr+2]  # check

                                            if n_num < n_n_num:
                                            curr=n_num
                                            else:
                                            curr=n_n_num

                                            cost += cur_num
                                            return
