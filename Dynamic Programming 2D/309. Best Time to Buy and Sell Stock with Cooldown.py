from typing import List

# Input: prices = [1,2,3,0,2] 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = float("-inf")
        held = float("-inf")
        reset = 0

        for p in prices:
            prevSold = sold
            sold = held + p
            held = max(held, reset - p)
            reset = max(reset, prevSold)
            
            print("=========p==========", p)
            print("prevSold:", prevSold)
            print("sold:", sold)
            print("held:", held)
            print("reset:", reset)
            
        return max(sold, reset)
    
s = Solution()
s.maxProfit([1,2,3,0,2])