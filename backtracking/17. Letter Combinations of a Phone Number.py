class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        temp = []

        def backtrack(next_digits):
            if not next_digits:
                res.append("".join(temp))
                return
            
            for letter in phone[next_digits[0]]:
                temp.append(letter)
                backtrack(next_digits[1:])
                temp.pop()
        
        backtrack(digits)
        return res