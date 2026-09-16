class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        n = len(arr)
        possible = 0
        last = 0
        while possible < n:
            if arr[last] == 0:
                possible += 2
            else:
                possible += 1
            last += 1

        last -= 1

        i = last
        j = n - 1

        while i >= 0:
            if arr[i] == 0:
                if possible > n:
                    arr[j] = 0
                    j -= 1
                    possible -= 1
                else:
                    arr[j] = 0
                    j -= 1
                    arr[j] = 0
                    j -= 1
                    possible -= 2
            else:
                arr[j] = arr[i]
                j -= 1
                possible -= 1

            i -= 1