class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        ans1 = []
        ans2 = []
        set1 = set(nums1)
        set2 = set(nums2)

        for n in set1:
            if n not in set2:
                ans1.append(n)

        for n in set2:
            if n not in set1:
                ans2.append(n)

        ans.append(ans1)
        ans.append(ans2)

        return ans
