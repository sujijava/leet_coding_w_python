class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number = number + translations[char]
        return number

s = Solution()
print(s.romanToInt("LVIII"))


'''
Summary:
It should be calculated with addition calculation only.
Remove subtract calculations.

Complexity:
 - Time: O(n): n the number of symbols
 - Space: O(1): translation dictionary is not increasing. constant.
'''


