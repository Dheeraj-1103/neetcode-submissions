class Solution:
    def twoSum(self, a: List[int], t: int) -> List[int]:
        d={}
        for i in range(len(a)):
            if t-a[i] in d:
                return [d[t-a[i]],i]
            d[a[i]]=i
        