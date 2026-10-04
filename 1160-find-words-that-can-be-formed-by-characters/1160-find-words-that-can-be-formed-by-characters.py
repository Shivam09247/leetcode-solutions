class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dic = {}

        for c in chars:
            dic[c] = dic.get(c, 0) + 1
        ans = 0
        for word in words:
            temp = {}

            for c in word:
                temp[c] = temp.get(c, 0) + 1

            good = True

            for c, count in temp.items():
                if c not in dic or count > dic[c]:
                    good = False
                    break

            if good:
                ans += len(word)

        return ans