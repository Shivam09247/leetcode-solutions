class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s=set(list([i for i in range(97,123)]))
        for i in sentence:
            if ord(i) in s:
                s.remove(ord(i))
        return len(s)==0
        