class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if nums == []: return nums
        m = len(nums)
        n = len(nums[0])
        
        if m*n != r*c: return nums
        
        reshaped = [[0 for i in range(c)] for j in range(r)]
        
        curr_i = 0
        curr_j = 0
        
        for i in nums:
            for j in i:
                if curr_j >= c:
                    curr_i += 1
                    curr_j = 0
                reshaped[curr_i][curr_j] = j
                curr_j += 1
        return reshaped
                