class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        ans = 0
        for word in text.split():
            if all(ch not in broken for ch in word):
                ans += 1

        return ans