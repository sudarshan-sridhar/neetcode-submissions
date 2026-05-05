from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        am=defaultdict(list)
        for s in strs:
            sorted_key= ''.join(sorted(s))
            am[sorted_key].append(s)
        return list(am.values())