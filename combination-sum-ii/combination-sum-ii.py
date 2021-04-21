from copy import copy

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # https://www.youtube.com/watch?v=IER1ducXujU&ab_channel=KevinNaughtonJr.
        candidates = sorted(candidates)
        self.ans = []
        
        def recurse(index, target, arr):
            if target == 0: 
                self.ans.append(copy(arr))
                return 
            
            for i in range(index,len(candidates)):
                if (i == index or candidates[i]!=candidates[i-1]) and candidates[i]<=target:
                    arr.append(candidates[i])
                    recurse(i+1,target-candidates[i],arr)
                    arr.pop()
                    
            return
        
        recurse(0,target,[])
        return self.ans