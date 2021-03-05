class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = {}
        ans = []
        for i in nums:
            if i not in m: m[i] = 1
            else: 
                ans.append(i)
                m[i] += 1
        for i in range(1,len(nums)+1):
            if i not in m:
                ans.append(i)
                break
        return ans