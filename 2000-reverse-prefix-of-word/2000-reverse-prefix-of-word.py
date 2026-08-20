class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        lst=[]
        for i in word:
            lst.append(i)
            if i==ch:
                lst=lst[::-1]
                ch=""
        return "".join(lst)
        