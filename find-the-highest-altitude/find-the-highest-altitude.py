class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = gain[0]
        for i in range(1,len(gain)):
            gain[i] = (curr+gain[i])
            curr = gain[i]
        gain.append(0)
        return max(gain)