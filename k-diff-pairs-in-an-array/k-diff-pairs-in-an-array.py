from collections import Counter

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c = Counter(nums)
        count = 0

        for i in c.keys():
            if k == 0:
                if c[i] >= 2:
                    count += 1
            else:
                if i-k in c:
                    count += 1
            
        return count