class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # subset means any combination of elements in the array (this is different from subarray and subsequence)
        # total sum is essentially (subset sum * 2)
        # so the prob we are trying to solve is finding one subset sum = total_sum/2
        # if one such subset exists that means another subset of equal sum also exists
        total_sum = sum(nums)
        memo = {}
        
        # at every step we either include the current element or ignore it
        # if we include the current element, we update the curr_sum value (= sum of all included elements so far)
        # if we exclude the current element, we keep the curr sum value as it is
        def recurse(i = 0, curr_sum = total_sum/2.0):
            if i >= len(nums): return False
            # target sum exceeded
            if curr_sum < 0: return False
            # target sum reached
            if curr_sum == 0: return True
            
            key = (i, curr_sum)
            if key in memo: return memo[key]
            
            # either include the current element in the subset or ignore it
            # if any of them return true means we know there exists such a subset
            memo[key] = recurse(i+1, curr_sum-nums[i]) or recurse(i+1, curr_sum)
            
            return memo[key]
        
        return recurse()