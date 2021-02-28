class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -pow(2,31) and divisor == -1: return pow(2,31)-1
        if dividend == 0: return 0
        neg = True
        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0): neg = False
        
        count = 0
        start = abs(divisor)
        target = abs(dividend)
        while target - start >= 0:
            x = 0
            while target - (start << 1 << x) >= 0:
                x += 1
            count += (1 << x)
            target -= (start << x)
        
        if neg: return 0 - count
        return count
        