# Two strings are considered close
# if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character
# into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2,
# return true if word1 and word2 are close, and false otherwise.


# -------------------------------------------------------------------
# Order does not matter for set; set {1,2,3} and {3,2,1} are equal
# Counter method
# map the occurrence

from collections import Counter


class Solution:
    def closeStrings(self, w1, w2):
        print(Counter(w1))
        print(Counter(w2))
        print(Counter(Counter(w1).values()))
        print(Counter(Counter(w2).values()))
        return set(w1) == set(w2) and Counter(Counter(w1).values()) == Counter(Counter(w2).values())


s = Solution()
s.closeStrings("abb", "aab")
