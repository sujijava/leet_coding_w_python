class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            l_height = height[left]
            r_height = height[right]

            curr_area = min(l_height, r_height) * (right - left)
            max_area = max(curr_area, max_area)

            if l_height < r_height:
                left = left + 1
            else:
                right = right - 1

        return max_area
