class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # kadane's algo
        max_sum = -sys.maxint - 1
        curr_sum = 0
        
        for i in (nums):
            curr_sum += i

            max_sum = max(max_sum, curr_sum)
            
            # throw away negative value
            curr_sum = max(curr_sum,0)
            
        
        return max_sum
        
        