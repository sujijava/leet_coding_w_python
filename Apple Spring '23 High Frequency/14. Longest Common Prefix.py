class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        # it starts from 1.
        # since str[0] is prefix itself.
        for i in range(1, len(strs)):
            # it checks whether prefix is in strs[i]
            # it checks whether prefix is in head not middle or tail.
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if len(prefix) == 0:
                    return ""
        return prefix

s = Solution()
print(s.longestCommonPrefix(["flower", "c"]))


'''
Summary:
Suppose prefix is first string.
Remove from the prefix as you iterate the strings array

Complexity:
 - Time: O(n): n is the number of chars in string array
 - Space: O(1):
'''
