class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = set()
        def dfs(i, count = 0):
            if nums[i] == i or nums[i] in visited: return count
            visited.add(nums[i])
            return dfs(nums[i], count + 1)
        
        m = 1
        for i in range(len(nums)):
            m = max(m,dfs(i))
        
        return m
        