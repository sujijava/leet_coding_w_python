# points = [[3,12],[-2,5],[-4,1]]
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        distanceMap = {i: [] for i in range(len(points))}
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                distance = abs(x2-x1) + abs(y2-y1)
                distanceMap[i].append([distance, j])
                distanceMap[j].append([distance, i])
        # distanceMap = {
        #               0: [[12, 1], [18, 2]],
        #               1: [[12, 0], [6, 2]],
        #               2: [[18, 0], [6, 1]]}

        # Prim's
        res = 0
        visited = set()
        minH = [[0, 0]]  # [cost, point]
        while len(visited) < N:
            minCost, minPoint = heapq.heappop(minH)
            if minPoint in visited:
                continue
            res += minCost
            visited.add(minPoint)
            for cost, index in distanceMap[minPoint]:
                if index not in visited:
                    heapq.heappush(minH, [cost, index])
        return res


points = [[3, 12], [-2, 5], [-4, 1]]
s = Solution()
s.minCostConnectPoints(points)

'''Summary
Logic Summary 
    1. The code starts with an arbitrary point. i.e. first point - [0,0]
    2. It iteratively selects the closest unvisited point and adds its distance to the result.
    3. This process continues until all points are visited, 
        and the code returns the minimum cost. 
        
Prim's
- Prim's algorithm is a greedy approach for finding a minimum spanning tree in a weighted graph.
- It starts from an arbitrary node and iteratively adds the closest unvisited node.
- The process continues until all nodes are included, 
    resulting in a tree with the minimum total edge weight.
'''
