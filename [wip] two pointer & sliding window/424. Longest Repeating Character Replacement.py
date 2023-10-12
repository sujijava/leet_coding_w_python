class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        left = 0
        right = 0
        maxFrequency = 0

        for right in range(len(s)):
            charMap[s[r]] = charMap.get([s[r]], 0)
            maxFrequency = max(maxFrequency, charMap[s[r]])

            if (right - left + 1) - maxFrequency > k:
                charMap[s[r]] -= 1
                left += 1
        return right - left + 1
