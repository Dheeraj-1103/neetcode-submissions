class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        a=[]
        for i in range(len(arr)):
            x=-1
            for j in range(i+1,len(arr)):
                x=max(arr[j],x)
            a.append(x)
        #a.append(-1)
        return a