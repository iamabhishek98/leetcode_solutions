from copy import copy

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.ans = set()
        def recurse(nums,target,curr):
            if target == 0: 
                self.ans.add(tuple(sorted(copy(curr)))) 
                return
            for i in nums:
                if i <= target: 
                    curr.append(i)
                    recurse(nums,target-i,curr)
                    curr.pop()
            
        recurse(candidates,target,[])
        return self.ans
        