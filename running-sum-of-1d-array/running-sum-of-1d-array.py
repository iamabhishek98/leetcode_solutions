class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = nums[0]
        for i in range(1,len(nums)):
            total += nums[i]
            nums[i] = total
        return nums