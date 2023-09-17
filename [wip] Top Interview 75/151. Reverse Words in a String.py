"  hello world  "


class Solution:
    def reverseWords(self, s: str) -> str:

        words = []
        index = 0
        ans = []
        for i in range(len(s)):
            char = s[i]
            if char == " " and i-1 >= 0 and s[i-1] != " ":
                index = index + 1
            elif char != " ":
                if index < len(words):
                    words[index] = words[index] + char
                else:
                    words.append(char)

        print(words)
        for j in range(len(words)):
            ans.append(words[len(words) - j - 1])

        return " ".join(ans)
