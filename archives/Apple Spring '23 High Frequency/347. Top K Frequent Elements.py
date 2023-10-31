from typing import List
import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapNums = collections.Counter(nums)

        # 2d array [[],[],[],...]
        # why len(nums) + 1??
        bucketSort = [[] for i in range(len(nums) + 1)]

        for key, value in mapNums.items():
            bucketSort[value].append(key)

        print(bucketSort)
        res = []
        for i in range(len(bucketSort) - 1, 0, -1):
            for n in bucketSort[i]:
                res.append(n)
                if len(res) == k:
                    return res


'''
Summary: Hashmap -> Bucket Sort! 

Complexity:
 - Time: O(N + M): 
    N = len(nums)
    M = len(map)
 - Space: O(M): M = len(map)
'''
