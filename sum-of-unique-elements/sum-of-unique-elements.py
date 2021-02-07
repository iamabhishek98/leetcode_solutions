class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        m = {}
        for i in nums:
            if i in m: m[i]+=1
            else: m[i] = 1
        ans = 0
        for i in m:
            if (m[i]==1): ans+=i
        return ans