import collections
import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f = collections.defaultdict(dict)
        # [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
        for source, destination, p in flights:
            f[source][destination] = p

        print(f)
        # {0: {1: 100},
        # 1: {2: 100,
        #     3: 600},
        # 2: {0: 100,
        #     3: 200}}
        heap = [(0, src, k + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1

s = Solution()
s.findCheapestPrice(3,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,2,1)
