class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums): return 0
        
        nums.sort()
        
        m = 1
        curr = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                curr += 1
                m = max(m, curr)
            elif nums[i] != nums[i-1]:
                curr = 1
        
        return m
        