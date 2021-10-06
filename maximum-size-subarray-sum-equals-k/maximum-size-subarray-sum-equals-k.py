class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # idea is to store all the current sums at every element of the array
        # if the current iterating sum is not equal to the target, 
        # we check if the difference already exists in the map and then compare
        curr_sum = 0
        max_len = 0
        sum_map = {}
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            
            if curr_sum == k:
                max_len = i+1
                
            elif curr_sum-k in sum_map:
                max_len = max(max_len, i-sum_map[curr_sum-k])
                
            if curr_sum not in sum_map:
                sum_map[curr_sum] = i
        
        return max_len