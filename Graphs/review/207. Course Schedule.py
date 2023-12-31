from typing import List


# numCourses = 2, prerequisites = [[1,0],[0,1]]
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
                return False
        return True
