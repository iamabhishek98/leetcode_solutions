class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ori = n
        if (n<=0): return False
        i = 0
        while(n>0):
            n/=3
            i+=1
        if (pow(3,i-1)==ori): return True
        return False