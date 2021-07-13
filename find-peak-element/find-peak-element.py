class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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