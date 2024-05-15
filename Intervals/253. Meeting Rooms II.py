# The maximum number of overlapping meetings 
# is equivalent to 
# the minimum number of required conference rooms.

def minMeetingRooms(self, intervals) -> int:
        meetings = []
        for start, end in intervals:
            meetings.append((start, 1))
            meetings.append((end, -1))
        meetings.sort()
        max_overlap, overlap = 0, 0
        for _ , offset in meetings:
            overlap += offset
            max_overlap = max(max_overlap, overlap)
        return max_overlap