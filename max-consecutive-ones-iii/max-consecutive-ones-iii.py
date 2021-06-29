class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start, end, max_len, curr_zeros = 0,0,0,0
        
        while end < len(nums):
            # if curr num is 0, curr=1
            curr = (nums[end]==0)
            
            # if the max no. of flipped 1s is still less than k, count can be incremented
            if curr_zeros+curr<=k:
                curr_zeros+=curr
                end+=1
                max_len = max(end-start, max_len)
            
            # else slide window forward, updating curr no. of zeroes until it becomes less than k
            else:
                # need to do this check because the start of the window could be a 1 or a 0
                # if it is 1, curr no. of zeroes remains the same, hence no change
                # only when it is 0, curr no. of zeroes decreases and the end of the window can increment
                curr_zeros-=(nums[start]==0)
                start+=1
            
        return max_len
            