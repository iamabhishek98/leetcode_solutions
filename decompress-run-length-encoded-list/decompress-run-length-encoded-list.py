class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        ans = []
        while i < len(nums)-1:
            a = nums[i]
            b = nums[i+1]
            for j in range(a):
                ans.append(b)
            i+=2
        return ans