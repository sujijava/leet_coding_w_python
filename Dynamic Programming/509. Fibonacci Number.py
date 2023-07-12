class Solution:
    cache = {0: 0, 1: 1}

    def fib(self, N: int) -> int:
        if N in self.cache:
            return self.cache[N]
        self.cache[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.cache[N]

    def fib_top_down(self, N: int) -> int:
        fibonacci_arr = [0, 1]

        for i in range(2, N+1):
            fibonacci_arr.append(fibonacci_arr[i-2] + fibonacci_arr[i-1])
        return fibonacci_arr[N]


s = Solution()
print(s.fib_top_down(3))

'''
Summary:
top_down: iteration 
bottom_up: recursion

Complexity:
 - Time: O(N)
 - Space: O(N)
'''
