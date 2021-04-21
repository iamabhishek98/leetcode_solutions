class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target >= nums[0]:
            prev = nums[0]
            for i in range(len(nums)):
                if prev > nums[i]: return -1
                if nums[i] == target: return i
        else:
            prev = nums[-1]
            for i in range(len(nums)-1,0,-1):
                if prev < nums[i]: return -1
                if nums[i] == target: return i
        return -1