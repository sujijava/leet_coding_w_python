# Given a string s and an integer k,
# return the maximum number of vowel letters
# in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Input: s = "abciiidef", k = 3
# Output: 3

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        current_count = 0
        max_count = 0

        for char in s[:k]:
            if char in vowels:
                current_count += 1

        for i in range(1, len(s)-k+1):
            if s[i-1] in vowels:
                current_count = current_count - 1

            if s[i-k+1] in vowels:
                current_count = current_count + 1

            max_count = max(current_count, max_count)

        return max_count
