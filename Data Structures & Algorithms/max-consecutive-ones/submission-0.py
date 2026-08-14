class Solution:
    def findMaxConsecutiveOnes(self, a: List[int]) -> int:
        m=0
        x=0
        for i in a:
            if i ==1:
                m+=1
            else:
                x=max(x,m)
                m=0
        x=max(x,m)
        return x
        
