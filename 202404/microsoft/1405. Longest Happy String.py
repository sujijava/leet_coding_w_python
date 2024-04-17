class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        count = collections.Counter({'a':a, 'b':b, 'c':c})
        res = ['']
        while True:
            (curr_char, _), (next_char, _) = count.most_common(2)
            
            # if it does repeat two times i.e. "aa"
            if curr_char == res[-1] == res[-2]:
                curr_char = next_char
                
            if not count[curr_char]:
                break
                
            res.append(curr_char)
            count[curr_char] -= 1            
        
        return ''.join(res)   