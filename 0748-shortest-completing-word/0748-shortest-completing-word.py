from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        required = Counter(
            ch.lower()
            for ch in licensePlate
            if ch.isalpha()
        )

        answer = None

        for word in words:
            count = Counter(word.lower())

            if all(count[ch] >= freq for ch, freq in required.items()):
                if answer is None or len(word) < len(answer):
                    answer = word

        return answer