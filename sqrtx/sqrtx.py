class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # binary search approach
        left = 0
        right = x
        while left<=right:
            mid = (left+right)/2
            val = mid**2
            if val == x:
                return mid
            if val > x:
                right = mid - 1
            else:
                left = mid + 1
        
        return right
            