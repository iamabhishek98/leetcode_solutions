from collections import Counter

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        freq = Counter(nums)
        ans = set()
        
        def addToAns(a,b,c,d):
            ans.add(tuple(sorted([a,b,c,d])))
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):            
                for k in range(j+1,len(nums)):
                    val = target-nums[k]-nums[j]-nums[i]
                    if val in freq:
                        if val == nums[k] == nums[j] == nums[i]:
                            if freq[val] >= 4: addToAns(val,nums[k],nums[j],nums[i])
                        elif val == nums[k] == nums[j] or val == nums[k] == nums[i] or val == nums[j] == nums[i]:
                            if freq[val] >= 3: addToAns(val,nums[k],nums[j],nums[i])
                        elif val == nums[k] or val == nums[j] or val == nums[i]:
                            if freq[val] >= 2: addToAns(val,nums[k],nums[j],nums[i])
                        else: addToAns(val,nums[k],nums[j],nums[i])
        
        return ans