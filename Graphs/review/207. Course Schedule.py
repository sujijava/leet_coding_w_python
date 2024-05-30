from typing import List


# numCourses = 2, prerequisites = [[1,0],[0,1]]
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        self.preMap = {c: [] for c in range(numCourses)}
        for c, p in prerequisites:
            self.preMap[c].append(p)

        self.verified, self.visiting = set(), set()
        for c in range(numCourses):
            if self. dfs(c) == False:
                return False
        return True
    
    def dfs(self, c):
        if c in self.visiting:
            return False
        if c in self.verified:
            return True

        self.visiting.add(c)
        for p in self.preMap[c]:
            if self.dfs(p) == False:
                return False
        self.visiting.remove(c)
        self.verified.add(c)
        return True
