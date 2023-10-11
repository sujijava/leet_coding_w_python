class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Represents course dependencies
        dependency_map = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            dependency_map[course].append(prerequisite)

        visited = set()  # Set to keep track of visited courses during DFS

        def dfs(course):
            if course in visited:
                return False
            if not dependency_map[course]:
                return True
            visited.add(course)
            for prerequisite_course in dependency_map[course]:
                if not dfs(prerequisite_course):
                    return False
            visited.remove(course)
            dependency_map[course] = []
            return True

        for current_course in range(numCourses):
            if not dfs(current_course):
                return False
        return True
