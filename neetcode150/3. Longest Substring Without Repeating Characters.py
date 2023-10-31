# Summary
# remember case "dvdf"
# remove char one by one.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_arr = []
        l = 0
        r = 0
        res = 0

        while r < len(s):
            cur_char = s[r]

            if cur_char in char_arr:
                char_arr = []
                l = r + 1

            char_arr.append(cur_char)

            res = max(r - l + 1, res)

            r = r+1
        return res


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         charSet = set()
#         l = 0
#         res = 0

#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l += 1
#             charSet.add(s[r])
#             res = max(res, r - l + 1)
#         return res


s = Solution()
s.lengthOfLongestSubstring("aab")
