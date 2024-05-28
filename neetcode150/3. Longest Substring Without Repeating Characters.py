# Summary
# remember case "dvdf"
# remove char one by one.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        counter = 1
        
        if len(s) == 0:
          return 0
        
        for r in range(1,len(s)): # r = 1 # r = 2
          while s[r] in s[l:r]: 
            # should include l and r characters    
              l += 1 # r = 1
          temp_counter = r - l + 1  # 1-0+1 = 2
          counter = max(temp_counter, counter) # 2 
        return counter

s = Solution()
s.lengthOfLongestSubstring("aab")
