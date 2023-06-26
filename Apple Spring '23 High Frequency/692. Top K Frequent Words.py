from typing import List
import collections

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        map = Collection.Counter(words)
        bucket_sort = [[] for i in range(len(words) + 1)]
        res = []

        for key, value in map.items():
            bucket_sort[value].append(key)

        for i in range(len(bucket_sort) - 1, 0, -1):
            for word in sorted(bucket_sort[i]):
                res.append(word)
                if k == len(res):
                    return res


s = Solution()
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))

'''
Summary: Hashmap -> Bucket Sort! 

Complexity:
 - Time: O(N + M + KlogK): 
    N = len(nums)
    M = len(map)
    K = the len of longest element in map ?? 
 - Space: O(M): M = len(map)
'''
