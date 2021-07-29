class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = [1]
        if n == 1: return arr
        
        for i in range(2,n+1):
            left = []
            right = []
            for j in arr:
                odd = 2*j-1
                even = 2*j
                if odd <= n:
                    left.append(odd)
                if even <= n:
                    right.append(even)
            
            arr = left + right
        
        return arr
                    
                    
                    