class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        # top down memoization approach
        dayset = set(days)
        durations = [1,7,30]
        memo = [-1]*366

        def recurse(i=0):
            if i > 365: return 0
            if memo[i] != -1: return memo[i]
            
            if i in dayset:
                m = sys.maxint
                # try out the costs for all the different durations-costs to get minimum
                for j in range(3):
                    duration_cost = costs[j] + recurse(i+durations[j])
                    m = min(m, duration_cost)
                memo[i] = m
            
            else: 
                memo[i] = recurse(i+1)
            
            return memo[i]
        
        return recurse()