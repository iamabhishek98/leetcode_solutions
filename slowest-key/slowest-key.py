class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        max_duration = releaseTimes[0]
        max_key = keysPressed[0]
        
        for i in range(1,len(releaseTimes)):
            curr_duration = releaseTimes[i] - releaseTimes[i - 1]
            if curr_duration > max_duration:
                max_duration = curr_duration
                max_key = keysPressed[i]
            elif curr_duration >= max_duration:
                max_key = max(max_key, keysPressed[i])

        return max_key