class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_gain = 0
        max_gain = 0

        for i in range(len(gain)):
            curr_gain = curr_gain + gain[i]
            max_gain = max(max_gain, curr_gain)

        return max_gain
