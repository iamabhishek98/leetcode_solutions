from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        m = Counter(nums)
        ans = 0
        for i in m:
            if (m[i]==1): ans+=i
        return ans