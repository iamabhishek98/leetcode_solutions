class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [-1]*101
        
        def recurse(i=0):
            if i >= len(nums): 
                return 0
            
            if memo[i] != -1: return memo[i]
            
            # either he steals from the next house
            # or in the current house skipping the next house
            memo[i] = max(recurse(i+1), nums[i] + recurse(i+2))
            
            return memo[i]
        
        
        return recurse()
