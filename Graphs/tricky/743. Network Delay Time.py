# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# k = source
# Output: 2

# We will send a signal from a given node k. 
# Return the minimum time it takes for all the n nodes 
# to receive the signal. 

import collections
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, root_src: int) -> int:
        edges = collections.defaultdict(list)
        for src, dst, time in times:
            edges[src].append((dst, time))
        # edges = {2: [(1, 1), (3, 1)], 3: [(4, 1)]}
        
        minHeap = [(0, root_src)]
        visit = set()
        res = 0
        while minHeap:
            curr_time, curr_node = heapq.heappop(minHeap)
            if curr_node in visit:
                continue
            visit.add(curr_node)
            res = curr_time

            for next_node, next_time in edges[curr_node]:
                if next_node not in visit:
                    heapq.heappush(minHeap, (curr_time + next_time, next_node))
        return res if len(visit) == n else -1

        # O(E * logV)

s = Solution()
s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)