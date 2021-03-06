class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 1 < len(nums) and nums[0] > nums[1]: return 0
        for i,x in enumerate(nums):
            if i == len(nums)-1:
                if x > nums[i-1]: return i
            elif nums[i-1] < x and nums[i+1] < x: return i
        return 0