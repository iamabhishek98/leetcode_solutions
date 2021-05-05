class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.dp = {}
        def recurse(index,hops):
            key = str(index)+":"+str(hops)
            if key in self.dp: return self.dp[key]
            if index >= len(nums)-1:
                return hops

            m = sys.maxint
            for i in range(1,nums[index]+1): m = min(m,recurse(index+i,hops+1))
            self.dp[key] = m
            return m
        
        return recurse(0,0)