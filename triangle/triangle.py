class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.m = sys.maxint
        self.dp = [{} for i in range(len(triangle))]
        
        def dfs(lvl,i,s): 
            if i in self.dp[lvl]:
                return self.dp[lvl][i]
            ans = triangle[lvl][i]
            if lvl < len(triangle)-1:
                ans += min(dfs(lvl+1,i,s),dfs(lvl+1,i+1,s))
            self.dp[lvl][i] = ans
            return ans
        
        return dfs(0,0,0)
        