class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        mini_curr = 0
        for big_curr in range(len(t)):
            big_curr_char = t[big_curr]
            mini_curr_char = s[mini_curr]

            if big_curr_char == mini_curr_char:
                mini_curr = mini_curr + 1

        return mini_curr == len(s)
