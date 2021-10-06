class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 1: return nums
        
        # get maxes within every block while iterating from left to right
        left_max = []
        for i in range(len(nums)):
            if i % k == 0:
                m = nums[i]
            else:
                m = max(m,nums[i])
            left_max.append(m)
        
        right_max = []
        # the last block may not be of length k, so we need to store the last element as initial value for m
        m = nums[-1]
        # get maxes within every block while iterating from right to left
        for i in range(len(nums)-1,-1,-1):
            if i % k == 0:
                m = nums[i]
            else:
                m = max(m,nums[i])
            right_max.append(m)
            
        right_max.reverse()
        
        output = []
        for i in range(0,len(nums)-k+1):
            # compare right and left max for each block and get the max 
            # because either one of them is guaranteed to have the max
            output.append(max(right_max[i], left_max[i + k - 1]))
        
        return output