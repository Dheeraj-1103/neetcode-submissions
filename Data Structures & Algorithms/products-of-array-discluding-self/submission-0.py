class Solution:
    def productExceptSelf(self, a: List[int]) -> List[int]:
        pre=[1]*(len(a))
        suf=[1]*(len(a))
        pre[0]=1
        suf[0]=1
        for i in range(1,len(a)):
            pre[i]=pre[i-1]*a[i-1]
        for i in range(len(a)-2,-1,-1):
            suf[i]=suf[i+1]*a[i+1]
        print(pre)
        print(suf)
        res=[0]*len(a)
        for i in range(len(a)):
            res[i]=pre[i]*suf[i]

        return res