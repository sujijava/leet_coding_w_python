class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(list("aeiouAEIOU"))
        s = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] in vowels and s[right] in vowels:
                left_char = s[left]
                right_char = s[right]
                s[left] = right_char
                s[right] = left_char
                left = left + 1
                right = right - 1
            if s[left] not in vowels:
                left = left + 1
            if s[right] not in vowels:
                right = right - 1

        return ''.join(s)
