from collections import Counter


class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = Counter(num)
        sorted_key = sorted(count.keys(), reverse=True)
        palindrome = ''
        mid = ''

        for d in sorted_key:
            if count[d] %2 == 1:
                mid = max(mid, d)
            palindrome += d * (count[d] // 2)

        palindrome = palindrome.lstrip('0')
        return (palindrome + mid + palindrome[::-1]) or '0'

s = Solution()
s.largestPalindromic("444947137")
