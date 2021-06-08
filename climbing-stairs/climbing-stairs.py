class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dp = {}

        def recurse(i):
            if i > n: return 0
            
            if i == n: 
                return 1

            if i in self.dp: 
                return self.dp[i]

            self.dp[i] = recurse(i+1)+recurse(i+2)
            
            return self.dp[i]
        
        return recurse(0)
