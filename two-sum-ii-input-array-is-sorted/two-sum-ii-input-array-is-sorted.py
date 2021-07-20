class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1

        while left<right:
            s = nums[left]+nums[right]
            if s<target: left+=1
            elif s>target: right-=1
            else:
                return [left+1,right+1]