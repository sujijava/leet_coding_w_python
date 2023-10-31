# n = 4,
# flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
# src = 0,
# dst = 3,
# k = 1

from typing import List

class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        prices = [float("inf")] * n
        # prices list records the minimum cost from the source node to each node in the graph.
        # Given the source node is 0
            # prices[0]: minimum cost from the 0 to 0
            # prices[1]: minimum cost from the 0 to 1
            # prices[2]: minimum cost from the 0 to 2
        prices[src] = 0
        # cause going src to src costs nothing

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:  # s=source, d=dest, p=price
                if prices[s] == float("inf"):
                    continue
                # checks if the minimum cost to reach the source node s is still infinity,
                # and if so, it skips the current flight because there is no valid path to s yet.
                if prices[s] + p < tmpPrices[d]:
                    # tmpPrices[d] represents the temporary minimum cost to reach the destination node d
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
            print(i) # 0, 1
            print(prices) # [0, 100, inf, inf], [0, 100, 200, 700]
        return -1 if prices[dst] == float("inf") else prices[dst]

s = Solution()
s.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)

'''
This code iterates through flights, tracking the cheapest path to dst while respecting the stop limit k.

Key values:
"prices": list
    - stores the minimum cost from source (0) to each node.
    - initialize prices with infinity, set src cost to 0.

For each stop (0 to k):
    - Create a temporary tmpPrices list.
    - Iterate through flights:
        - If prices to source node (s) is still infinity, skip, cause there is no valid path to s yet.
        - Update tmpPrices with the minimum cost to reach destination (d).
    - Update prices with tmpPrices.

Return -1 if no valid path to dst, else, return cost to reach dst.
'''
