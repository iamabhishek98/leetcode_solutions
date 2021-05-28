class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        s = dict()
        prev = 0
        i = 0
        m = 0
        for i,x in enumerate(nums):
            if x in s:
                index = s[x]
                while (prev<=index):
                    del s[nums[prev]]
                    curr-=nums[prev]
                    prev += 1
            curr += x
            s[x] = i
            m = max(m,curr)
        return m        