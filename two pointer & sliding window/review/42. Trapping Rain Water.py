# review needed for CONSTANT MEMORY solution
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left = 0
        right = len(height) - 1
        res = 0
        leftMax = height[left]
        rightMax = height[right]

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                currArea = leftMax - height[left]
                res += currArea
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                currArea = rightMax - height[right]
                res += currArea
        return res
