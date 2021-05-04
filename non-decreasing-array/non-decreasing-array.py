class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i+1]:
                count += 1
                if nums[i-1]>nums[i+1]: 
                    nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i+1]
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]: 
                count += 1
        
        return count <= 1