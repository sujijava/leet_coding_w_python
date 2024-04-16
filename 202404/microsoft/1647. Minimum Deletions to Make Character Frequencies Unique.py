class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s) # {a:3, b:3, c:2}
        values = counter.values() # [3,3,2]
        uniq_set = set() 
        output = 0 
    
        for v in values:
            # v = values[i] # 3 # 3 #2
            while v in uniq_set and v>0:
                v -= 1 #2 #1
                output += 1 #1 #2
            uniq_set.add(v) # (3,2,1)
        
        return output
