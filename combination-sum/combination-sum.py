from copy import copy

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # https://www.youtube.com/watch?v=IER1ducXujU&ab_channel=KevinNaughtonJr.
        candidates = sorted(candidates)
        self.ans = set()
        
        def recurse(target = target, arr = []):
            if target == 0: 
                self.ans.add(tuple(sorted(arr)))
                return 
            
            for i in range(len(candidates)):
                if candidates[i] <= target:
                    arr.append(candidates[i])
                    recurse(target-candidates[i],arr)
                    arr.pop()
                    
            return
        
        recurse()
        return self.ans