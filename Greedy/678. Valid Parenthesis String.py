# (*(
class Solution:
    def checkValidString(self, s: str) -> bool:
        remaining_open_min = remaining_open_max = 0

        for c in s:
            if c == '(':
                remaining_open_min += 1
                remaining_open_max += 1
            elif c == ')':
                if remaining_open_min > 0:
                    remaining_open_min -= 1 # with asterisk
                remaining_open_max -= 1
            elif c == '*':
                if remaining_open_min > 0:
                    remaining_open_min -= 1 # cuz it can be "("
                remaining_open_max += 1 # cuz it can be ")"

            if remaining_open_max < 0:
                return False

        return remaining_open_min == 0

s = Solution()
res = s.checkValidString("(*)")
print(res)
