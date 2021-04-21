from copy import copy

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # https://www.youtube.com/watch?v=IER1ducXujU&ab_channel=KevinNaughtonJr.
        candidates = [i for i in range(1,10)]
        self.ans = []
        
        def recurse(index, target, arr):
            if target == 0 and len(arr) == k: 
                self.ans.append(copy(arr))
                return 
            
            for i in range(index,len(candidates)):
                if (i == index or candidates[i]!=candidates[i-1]) and candidates[i]<=target:
                    arr.append(candidates[i])
                    recurse(i+1,target-candidates[i],arr)
                    arr.pop()
                    
            return
        
        recurse(0,n,[])
        return self.ans