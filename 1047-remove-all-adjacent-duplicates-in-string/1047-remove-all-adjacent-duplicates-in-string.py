class Solution:
    def removeDuplicates(self, s: str) -> str:
        lst=[]
        for i in s:
            if lst and lst[-1]==i:
                lst.pop()
            else:
                lst.append(i)
        return "".join(lst)
        