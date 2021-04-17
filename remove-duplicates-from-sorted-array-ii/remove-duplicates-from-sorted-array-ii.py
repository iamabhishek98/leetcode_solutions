class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        i = 0
        while i < len(nums):
            if i>0:
                if nums[i] == nums[i-1]:
                    count += 1
                else:
                    count = 0
            if count > 1: nums.pop(i)
            else: i+=1
            
            