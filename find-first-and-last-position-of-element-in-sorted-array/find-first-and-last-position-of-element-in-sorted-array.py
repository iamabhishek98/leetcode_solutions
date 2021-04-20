class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first_pos = last_pos = -1
        for i,x in enumerate(nums):
            if x == target:
                if first_pos == -1:
                    first_pos = i
                    last_pos = i
                else:
                    last_pos = i
        if first_pos == -1: return [-1,-1]
        return [first_pos,last_pos]
        