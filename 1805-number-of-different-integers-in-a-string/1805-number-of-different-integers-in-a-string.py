class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s=set()
        w=""
        for i in word:
            if 48<=ord(i)<=57:
                w+=i
            else:
                if w:
                    s.add(int(w))
                    w=""
        if w:
            s.add(int(w))
        return len(s)