import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s in strs:
            counts = [0] * 27
            for c in s:
                counts[ord("z") - ord(c)] += 1
                
            res[tuple(counts)].append(s) 

        return list(res.values())