class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        a = ["a", "e", "i", "o", "u","A","E","I","O","U"]
        s = list(s)
        while i < j:
            if s[i] not in a:
                i += 1
            elif s[j] not in a:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)