class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_left = nums[0]
        left = []
        
        min_right = nums[-1]        
        right = [0]*len(nums)
        
        for i in range(len(nums)):
            max_left = max(max_left, nums[i])
            left.append(max_left)    
        
        for i in range(len(nums)-1,-1,-1):
            min_right = min(min_right, nums[i])
            right[i] = min_right
        
        for i in range(1,len(nums)):
            # the prev max should be less than the current min 
            # because we dont want to insert the current element into the arr before checking that
            if left[i-1] <= right[i]: return i
            
        