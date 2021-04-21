class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.dp = {}
        def recurse(nums,target):
            if target == 0: return 1
            ans = 0
            if target in self.dp: return self.dp[target]
            for i in nums:
                if i <= target: ans+=recurse(nums,target-i)
            self.dp[target] = ans
            return ans
       
        return recurse(nums,target)
        