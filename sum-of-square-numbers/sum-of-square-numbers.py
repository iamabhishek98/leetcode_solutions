class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        j = math.floor(math.sqrt(c))
        
        if j**2 == c: return True        
        
        i = 1
        while i <= j:
            if i**2 + j**2 == c: return True
            elif i**2 + j**2 < c:
                i += 1
            else:
                j -= 1
                
        return False