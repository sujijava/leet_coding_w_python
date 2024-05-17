class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        used_rooms = 0
        end_pointer = 0
        start_pointer = 0

        # start_timings = [0,5,15]
        # end_timings = [10,20,30]

        while start_pointer < L:
            # not overlap
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                used_rooms -= 1
                end_pointer += 1
            # overlap
            used_rooms += 1    
            start_pointer += 1   

        return used_rooms