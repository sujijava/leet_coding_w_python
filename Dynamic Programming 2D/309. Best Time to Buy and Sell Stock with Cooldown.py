class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0

        can_buy = [0] * len(prices) # can buy
        can_sell = [0] * len(prices) # can sell
        will_rest = [0] * len(prices) # take a rest

        can_sell[0] = -prices[0]
        can_buy[0] = 0
        will_rest[0] = float('-inf')

        for i in range(1, len(prices)):
            can_buy[i] = max(can_buy[i - 1], will_rest[i - 1])
            # Stay at can_buy, or rest from will_rest
            # can buy, ie, we have no stock now, and the max profit should be ''last no stock profit'' or ''last rest profit''
            can_sell[i] = max(can_sell[i - 1], can_buy[i - 1] - prices[i])
            # can sell, ie, we now have stock, and the profit should be ''last stock profit'' or ''last no stock but buy this time''
            will_rest[i] = can_sell[i - 1] + prices[i]
             # Only one way from can_sell  //we should sell then take a rest

        return max(can_buy[-1], will_rest[-1])
