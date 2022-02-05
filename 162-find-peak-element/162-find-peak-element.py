class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Method 1
        start = 0
        end = len(nums)-1
        
        # if current element is greater than next element, keep moving backward
        # else if current element is smaller than next element, move forward
        # this way the position always converges to a peak
        while start<end:
            mid = (start+end)/2
            if nums[mid]>nums[mid+1]: end = mid
            else: start = mid+1
        
        return start
    
#         # Method 2
#         if len(nums) == 1: return 0
#         if len(nums) > 1: 
#             if nums[0] > nums[1]: return 0
#             if nums[-1] > nums[-2]: return len(nums)-1
        
#         left = 0
#         right = len(nums)-1
#         while left < right:
#             mid = (left+right)/2
#             if mid < len(nums)-1 and nums[mid] >= nums[mid+1]: 
#                 right = mid
#             elif mid < len(nums)-1 and nums[mid] <= nums[mid+1]:
#                 left = mid + 1
#         return left
        