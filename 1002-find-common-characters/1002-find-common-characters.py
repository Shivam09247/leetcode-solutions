class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dic = {}

        for ch in words[0]:
            dic[ch] = dic.get(ch, 0) + 1

        for word in words[1:]:
            current = {}

            for ch in word:
                current[ch] = current.get(ch, 0) + 1

            for ch in list(dic):
                if ch in current:
                    dic[ch] = min(dic[ch], current[ch])
                else:
                    del dic[ch]

        answer = []

        for ch, count in dic.items():
            for _ in range(count):
                answer.append(ch)

        return answer