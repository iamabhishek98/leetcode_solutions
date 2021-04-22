class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        snums = sorted(nums)
        ans = []
        for i in nums:
            ans.append(snums.index(i))
        return ans
        