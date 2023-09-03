# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        h = n
        while l <= h:
            m = (l + h) // 2
            if guess(m) == -1:
                h = m - 1
            elif guess(m) == 0:
                return m
            elif guess(m) == 1:
                l = m + 1
        return -1


class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        h = n
        while l <= h:  # Updated condition to allow l to equal h
            m = (l + h) // 2
            res = guess(m)
            if res == 0:
                return m
            elif res == -1:
                h = m - 1  # Adjust the upper bound
            elif res == 1:
                l = m + 1  # Adjust the lower bound
        return -1  # This line is just a fallback, ideally should never be reached
