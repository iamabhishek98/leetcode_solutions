class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if target >= nums[0]:
            prev = nums[0]
            for i in range(len(nums)):
                if prev > nums[i]: return False
                if nums[i] == target: return True
        else:
            prev = nums[-1]
            for i in range(len(nums)-1,0,-1):
                if prev < nums[i]: return False
                if nums[i] == target: return True
        return False