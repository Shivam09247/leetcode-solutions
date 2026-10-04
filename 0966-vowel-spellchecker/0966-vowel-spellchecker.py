class Solution:
    def spellchecker(self, wordlist, queries):
        exact = set(wordlist)
        case_map = {}
        vowel_map = {}

        def normalize(word):
            word = word.lower()
            return ''.join('*' if c in 'aeiou' else c for c in word)
        for word in wordlist:
            lower = word.lower()
            if lower not in case_map:
                case_map[lower] = word

            pattern = normalize(word)
            if pattern not in vowel_map:
                vowel_map[pattern] = word

        ans = []

        for query in queries:
            if query in exact:
                ans.append(query)
                continue
            lower = query.lower()
            if lower in case_map:
                ans.append(case_map[lower])
                continue
            pattern = normalize(query)
            if pattern in vowel_map:
                ans.append(vowel_map[pattern])
            else:
                ans.append("")

        return ans