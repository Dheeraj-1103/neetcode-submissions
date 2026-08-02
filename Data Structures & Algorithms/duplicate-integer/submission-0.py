from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        f=Counter(nums)
        for i,j in f.items():
            if j>1:
                return True
        return False