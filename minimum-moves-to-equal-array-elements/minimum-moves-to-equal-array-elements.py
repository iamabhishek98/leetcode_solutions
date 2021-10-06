class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # adding 1 to n-1 elements is the same as subtracting 1 from 1 element
        curr_min = min(nums)
        
        min_steps = 0
        for i in nums:
            min_steps += (i-curr_min)
        
        return min_steps