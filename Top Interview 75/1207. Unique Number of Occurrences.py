class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_map = {}
        for num in arr:
            if num in num_map:
                num_map[num] += 1
            else:
                num_map[num] = 1

        occurrences = num_map.values()
        return len(occurrences) > len(set(occurrences))
