class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n >= 0:
            count += 1
            n-=count
        if n<0: return count-1
        return count
                