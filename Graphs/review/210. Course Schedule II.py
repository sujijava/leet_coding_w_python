# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {c: [] for c in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)

        output = []
        verified, visiting = set(), set()

        def dfs(c):
            if c in visiting:
                return False
            if c in verified:
                return True

            visiting.add(c)
            for p in preMap[c]:
                if dfs(p) == False:
                    return False
            visiting.remove(c)
            verified.add(c)
            output.append(c)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
