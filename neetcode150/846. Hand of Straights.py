from collections import Counter
import heapq
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        counter = Counter(hand)
        minH = list(counter.keys())
        heapq.heapify(minH)

        while minH:
            start = minH[0]
            for i in range(start, start + groupSize):
                if counter[i] == 0 or i not in counter:
                    return False
                elif counter[i] == 1:
                    counter[i] -= 1
                    heapq.heappop(minH)
                elif i in counter:
                    counter[i] -= 1
        return True
