class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0 for _ in range(len(nums))]
        
        for i,x in enumerate(nums):
            ans[i] = nums[nums[i]]
            
        return ans
        