class Solution:
    def topKFrequent(self, a: List[int], k: int) -> List[int]:
        d={}
        for i in a:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        res = dict(sorted(d.items(), key=lambda item: item[1],reverse=True))
        print(res)
        r=list(res.keys())
        
        return r[:k]