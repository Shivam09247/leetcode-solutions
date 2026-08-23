class Solution:
    def makeGood(self, s: str) -> str:
        lst=[]
        for i in s:
            if lst and abs(ord(lst[-1])-ord(i))==32:
                lst.pop()
            else:
                lst.append(i)
        return "".join(lst)