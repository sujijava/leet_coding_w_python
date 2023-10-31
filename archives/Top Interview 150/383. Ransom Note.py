class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_hash = {}

        for i in range(len(magazine)):
            char = magazine[i]
            if char in magazine_hash:
                magazine_hash[char] = magazine_hash[char] + 1
            else:
                magazine_hash[char] = 1

        for i in range(len(ransomNote)):
            char = ransomNote[i]
            print(char)
            if char in magazine_hash and magazine_hash[char] >= 1:
                magazine_hash[char] = magazine_hash[char] - 1
                deleted = ransomNote.replace(char, "", 1)

        return deleted == ""


s = Solution()
print(s.canConstruct("abb", "aaa"))
