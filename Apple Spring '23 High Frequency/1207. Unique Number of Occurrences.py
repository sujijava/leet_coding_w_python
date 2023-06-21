from typing import List
import collections

class Solution(object):
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)
        print(c)
        print(c.values())
        return len(c) == len(set(c.values()))

s = Solution()
print(s.uniqueOccurrences([1, 2, 3]))


'''
Summary: Compare if
the numbers of distinct chars
=== distinct counts.

Complexity:
 - Time: O(n + k)
 - Space: O(k)
'''
