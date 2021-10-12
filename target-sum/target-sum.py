class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = {}
        def recurse(i = 0, curr_sum = 0):
            if i == len(nums):
                if curr_sum == target: return 1
                return 0
            
            key = (i,curr_sum)
            if key in memo: return memo[key]
            
            memo[key] = recurse(i+1,curr_sum+nums[i]) + recurse(i+1,curr_sum-nums[i])
            
            return memo[key]
        
        return recurse()