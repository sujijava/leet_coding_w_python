# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# [0, 1, 1, 2, 4, 7, 13, ... ]

class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0, 1, 1]
        if n <= 3:
            return arr[n]

        # if it's 4, i is 0 then done
        for i in range(n - 2):
            next_number = arr[i] + arr[i+1] + arr[i+2]
            arr.append(next_number)

        return arr[-1]


s = Solution()
print(s.tribonacci(4))
