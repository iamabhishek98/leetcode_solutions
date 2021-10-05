class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        curr_sum = 0
        min_len = sys.maxint
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while curr_sum >= target:
                min_len = min(min_len, right-left+1)
                curr_sum -= nums[left]
                left += 1
        
        return 0 if min_len == sys.maxint else min_len