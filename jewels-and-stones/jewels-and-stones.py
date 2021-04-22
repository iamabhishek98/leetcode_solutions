from collections import Counter

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        m = Counter(jewels)
        count = 0
        for i in range(len(stones)):
            if stones[i] in m: count+=1
        return count