class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k=s.strip()
        a=k.split(' ')
        print(a)
        return len(a[-1])