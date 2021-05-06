class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # https://www.youtube.com/watch?v=Zb4eRjuPHbM&ab_channel=NickWhite
        lastGoodIndex = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= lastGoodIndex:
                lastGoodIndex = i
        return lastGoodIndex == 0
        