class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        self.dp = {}
        def recurse(i):
            if i <= 1: return 0
            
            if i in self.dp: return self.dp[i]
            
            # try step 1 and step 2 and then take minimum
            self.dp[i] = min(cost[i-1]+recurse(i-1),cost[i-2]+recurse(i-2))
            
            return self.dp[i]
        
        return recurse(len(cost))