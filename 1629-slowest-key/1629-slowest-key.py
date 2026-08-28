class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_duration = releaseTimes[0]
        answer = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            if duration > max_duration:
                max_duration = duration
                answer = keysPressed[i]
            elif duration == max_duration and keysPressed[i] > answer:
                answer = keysPressed[i]

        return answer