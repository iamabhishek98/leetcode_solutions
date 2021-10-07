class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # method 1: divide repeatedly
        ori = n
        if (n<=0): return False
        i = 0
        curr = 1
        while(n>0):
            n/=3
            if i != 0: curr *= 3
            i+=1
            
        if (curr==ori): return True
        return False