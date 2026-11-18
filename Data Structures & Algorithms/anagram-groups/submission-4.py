import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s in strs:
            res[str(sorted(s))].append(s) 

        return list(res.values())