class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = -sys.maxint+1
        end = -sys.maxint+1
        m = -sys.maxint+1
        for i,x in enumerate(nums):
            if i < len(nums)-1 and x > nums[i+1] and start == -sys.maxint+1:
                start = i
                t = i - 1
                while t >= 0 and x == nums[t]:
                    start = t
                    t-=1
                    
            else:
                if x < m:
                    end = i
                    t = start - 1
                    while t >= 0 and x < nums[t]:
                        start = t
                        t-=1
            if x > m:
                m = x
        if start == -sys.maxint+1: return 0
        if end == -sys.maxint+1: return len(nums) - start
        return end-start+1
                