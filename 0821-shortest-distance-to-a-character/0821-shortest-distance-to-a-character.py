class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        ans = [n] * n
        prev = -n
        for i in range(n):
            if s[i] == c:
                prev = i
            ans[i] = i - prev

        next_pos = 2 * n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                next_pos = i
            ans[i] = min(ans[i], next_pos - i)

        return ans