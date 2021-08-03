class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # https://leetcode.com/problems/subsets-ii/discuss/1380366/Java-or-Python-or-Recursion-Visualization
        
        nums.sort()
        
        ps = []
        
        def backtrack(index=0,arr=[]):
            ps.append(tuple(arr))
            
            for i in range(index,len(nums)):
                # remove duplicates
                if i != index and nums[i] == nums[i-1]: 
                    continue
                arr.append(nums[i])
                backtrack(i+1, arr)
                arr.pop()
                
        backtrack()
        
        return ps