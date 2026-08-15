class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=0
        for i in s[::-1]:
            if i!=" ":
                l+=1
            if l>0 and i==" ":
                return l
        return l