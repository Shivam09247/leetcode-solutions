class Solution:
    def oddCells(self, m, n, indices):
        row = [0] * m
        col = [0] * n
        for r, c in indices:
            row[r] += 1
            col[c] += 1

        odd_rows = sum(x % 2 for x in row)
        odd_cols = sum(x % 2 for x in col)

        return odd_rows * (n - odd_cols) + (m - odd_rows) * odd_cols