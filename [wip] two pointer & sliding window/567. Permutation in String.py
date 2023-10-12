# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true

# summary:
# permutation conditions
# 1. the substring's length == s1 length
# 2. the substring should have every char in s1

# caution
# if "a,a,a,a" counter is 1.
# if "a,a,a,b" counter is 2.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = char_counter(s1)
        char_counter = 0
        window_len = len(s1)

        for i in range(len(s2)):
            entering_char = s2[i]
            if entering_char in s1_map:
                s1_map[entering_char] -= 1
                if s1_map[entering_char] == 0:
                    char_counter += 1

            if i >= window_len:
                leaving_char = s2[i-window_len]
                if leaving_char in s1_map:
                    if s1_map[leaving_char] == 0:
                        char_counter -= 1
                    s1_map[leaving_char] += 1

            if char_counter == len(s1_map):
                return True

        return False
