class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, target, [], res)

    def dfs(self, candidates, target, path, res):
        if target == 0:
            res.append(path)
            return
        for i in range(len(candidates)):
            if candidates[i] > target:
                continue
            self.dfs(candidates[i:],
                     target - candidates[i],
                     path+[candidates[i]],
                     res)


'''
Summary:
Review needed. not familiar yet with recursion 

Complexity:
 - Time: ?? 
 - Space: ?? 
'''
