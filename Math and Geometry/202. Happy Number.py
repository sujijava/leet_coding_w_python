# n = 19
class Solution:
    def isHappy(self, n: int) -> bool:
        res_set = set()
        while n != 1:
            tmp = 0 
            for i in str(n):
                tmp = tmp + (i**2)
            n = tmp 
            if n in res_set:
                return False 
            else:
                res_set.add(n)
        return True