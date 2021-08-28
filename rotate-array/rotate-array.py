from collections import deque

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        rotated = deque(nums)
        for i in range(k % len(nums)):
            rotated.appendleft(rotated.pop())
        
        for i in range(len(nums)):
            nums[i] = rotated[i]