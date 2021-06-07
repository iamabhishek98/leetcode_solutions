class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        maxlen = 0
        for i in nums:
            if i-1 not in s:
                currlen = 1
                currnum = i
                
                while currnum+1 in s:
                    currnum+=1
                    currlen+=1
                    
                maxlen = max(maxlen,currlen)
                
        return maxlen