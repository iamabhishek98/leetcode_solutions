class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for i in nums:
            if i not in freq: freq[i] = 1
            else: freq[i]+=1
            if freq[i]>len(nums)/2: return i
        