class Solution:
    cache = {0: 0, 1: 1, 2: 1, 3: 2}

    def tribonacci(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.tribonacci(
            n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        return self.cache[n]

    def tribonacci_top_down(self, n: int) -> int:
        arr = [0, 1, 1]
        for i in range(3, n+1):
            arr.append(arr[i-3] + arr[i-2] + arr[i-1])
        return arr[n]


s = Solution()
print(s.tribonacci(4))
