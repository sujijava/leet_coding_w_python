from heapq import heappop, heappush


class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        heap = []
        for i in range(len(heights) - 1):
            jump_needed = heights[i+1] - heights[i]
            if jump_needed <=0: continue

            # logN
            heappush(heap, jump_needed)

            if ladders < len(heap):
                # logN
                bricks = bricks - heappop(heap)

            if bricks < 0:
                return i
        return len(heights) - 1


s = Solution()
print(s.furthestBuilding([4,12,2,7,3,18,20,3,19],10,2))



'''
Summary:
Find the times where minimum amount bricks used.
Add gaps to heap
Pop out gaps from heap to find the minimum gaps available
if ladders < len(heap) -- to determine when to start use bricks

Complexity:
 - Time: P(N*logK)
 - Space: O(K) // K = len(heap)
'''
