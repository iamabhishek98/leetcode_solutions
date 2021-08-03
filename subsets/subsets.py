class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        
        ps = []
        
        def backtrack(index=0,arr=[]):
            ps.append(tuple(arr))
            for i in range(index,len(nums)):
                arr.append(nums[i])
                backtrack(i+1,arr)
                arr.pop()
                
        backtrack()
        
        return ps