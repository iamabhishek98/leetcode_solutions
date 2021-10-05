class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum = 0
        right_sum = sum(nums)
        
        for pivot in range(len(nums)):
            # we want to exclude the current element as that could possibly be the pivot
            right_sum -= nums[pivot]
            
            if pivot > 0:
                # to account for the sum of the elements on the left of the pivot
                left_sum += nums[pivot-1]
            
            # if this is the case we have found the pivot
            if left_sum == right_sum: return pivot  

        return -1