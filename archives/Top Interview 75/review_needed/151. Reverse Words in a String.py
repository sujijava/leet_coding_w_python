# Input: s = "the sky is blue"
# Output: "blue is sky the"


class Solution:
    def reverseWords(self, s: str) -> str:

        words = []
        index = 0
        ans = []
        for i in range(len(s)):
            char = s[i]
            if char == " " and i >= 1 and s[i-1] != " ":
                index = index + 1
            elif char != " ":
                if index < len(words):
                    words[index] = words[index] + char
                    print(char)
                    print(index)
                    print(words)
                else:
                    words.append(char)

        print(words)
        for j in range(len(words)):
            ans.append(words[len(words) - j - 1])

        return " ".join(ans)


s = Solution()
s.reverseWords("the sky is blue")
