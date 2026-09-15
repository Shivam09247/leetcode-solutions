class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)

        athletes = sorted(
            [(score[i], i) for i in range(n)],
            reverse=True
        )

        answer = [""] * n

        for rank, (_, index) in enumerate(athletes, start=1):
            if rank == 1:
                answer[index] = "Gold Medal"
            elif rank == 2:
                answer[index] = "Silver Medal"
            elif rank == 3:
                answer[index] = "Bronze Medal"
            else:
                answer[index] = str(rank)

        return answer