class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        x = 0
        for i in range(len(n)):
            x = max(int(n[i]),x)
        return x
        