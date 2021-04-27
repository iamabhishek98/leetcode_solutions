class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        powers = set()
        powers.add(1)
        curr = 1
        for i in range(1291):
            powers.add(curr*3)
            curr*=3
        return n in powers