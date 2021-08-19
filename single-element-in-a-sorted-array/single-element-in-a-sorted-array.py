class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right)/2
            if mid > 0 and nums[mid] == nums[mid-1]:
                if mid % 2 != 0: left = mid + 1
                else: right = mid - 1
            elif mid < len(nums)-1 and nums[mid] == nums[mid+1]:
                if mid % 2 != 0: right = mid - 1
                else: left = mid + 1
            else:
                return nums[mid]
        
        