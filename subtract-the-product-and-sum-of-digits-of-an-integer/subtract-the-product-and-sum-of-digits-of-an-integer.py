class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        p = 1
        while n>0:
            digit = n%10
            p *= digit
            s += digit
            n/=10
        return p-s