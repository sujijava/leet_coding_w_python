class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        child_id = 0

        for cookie_id in range(len(s)):
            if child_id < len(g) and s[cookie_id] >= g[child_id]:
                child_id += 1
            if child_id >= len(g):
                break

        return child_id
