class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        # in case the arr was not rotated
        m = nums[0]
        
        while left <= right:
            mid = (left+right)/2
            
            # check minimum at every point
            m = min(m, nums[mid])
                
            # greater than left means mid is the rotated part so need to go to the right
            if nums[mid] >= nums[0]:
                left = mid + 1
            
            # smaller than left means mid is in the unrotated part and needs to go to the left
            else:
                right = mid - 1
        
        return m