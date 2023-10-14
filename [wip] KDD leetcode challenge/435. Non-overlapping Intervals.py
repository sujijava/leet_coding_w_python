class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sortedIntervals = sorted(intervals, key=lambda x: x[1])
        prevEnd = -float('inf')
        counter = 0

        for currStart, currEnd in sortedIntervals:
            if prevEnd <= currStart:
                prevEnd = currEnd
            else:
                counter += 1

        return counter
