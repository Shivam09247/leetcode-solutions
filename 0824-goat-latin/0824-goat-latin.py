class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        words = sentence.split()

        result = []

        for i, word in enumerate(words, start=1):
            if word[0] in vowels:
                converted = word + "ma"
            else:
                converted = word[1:] + word[0] + "ma"

            converted += "a" * i
            result.append(converted)

        return " ".join(result)