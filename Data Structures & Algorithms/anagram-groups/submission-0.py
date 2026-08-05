from collections import defaultdict
class Solution:
    def groupAnagrams(self, a: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for i in a:
            x=tuple(sorted(i))    
            d[x].append(i)
        print(dict(d))
        return list(d.values())