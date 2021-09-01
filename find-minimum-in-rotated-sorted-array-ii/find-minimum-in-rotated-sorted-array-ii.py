class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        while left < right:
            # to remove duplicates
            while left < right and nums[left] == nums[left+1]: left += 1
            while left < right and nums[right] == nums[right-1]: right -= 1
                
            mid = (left+right)/2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            
            else:
                right = mid
        
        return nums[right]