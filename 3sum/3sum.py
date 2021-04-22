from collections import Counter

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        m = Counter(nums)
        ans = set()
        for i,x in enumerate(nums):
            for j in range(i+1,len(nums)):
                curr = (x+nums[j])*-1
                if curr in m:
                    if (curr == x and curr == nums[j] and m[curr]>2) or (((curr == nums[j] and curr != x) or (curr == x and curr != nums[j])) and m[curr]>1) or (curr!=x and curr!=nums[j]):
                        ans.add(tuple(sorted([x,nums[j],curr])))


        return ans