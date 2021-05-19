class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mid = len(nums)/2
        if len(nums)%2==0:
            ans1 = 0
            ans2 = 0
            for i in nums:
                ans1 += abs(i-nums[mid])
                ans2 += abs(i-nums[mid-1])
            return min(ans1,ans2)
        else:
            ans = 0
            mid = int(mid)
            for i in nums:
                ans += abs(i-nums[mid])
            return ans