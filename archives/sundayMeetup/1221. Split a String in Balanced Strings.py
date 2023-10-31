class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_counter = 0
        r_counter = 0
        res = 0

        for char in s:
            if char == "L":
                l_counter += 1
                if l_counter == r_counter:
                    res += 1
                    l_counter = 0
                    r_counter = 0
            elif char == "R":
                r_counter += 1
                if l_counter == r_counter:
                    res += 1
                    l_counter = 0
                    r_counter = 0

        return res


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_counter = 0
        r_counter = 0
        res = 0

        for char in s:
            if char == "L":
                l_counter += 1
            elif char == "R":
                r_counter += 1

            if l_counter == r_counter:
                res += 1

        return res
