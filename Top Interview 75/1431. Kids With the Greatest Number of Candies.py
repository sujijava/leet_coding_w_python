class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        max = candies[0]
        res = []

        for n in candies:
            if n >= max:
                max = n

        for n in candies:
            if extraCandies + n >= max:
                res.append(True)
            else:
                res.append(False)

        return res
