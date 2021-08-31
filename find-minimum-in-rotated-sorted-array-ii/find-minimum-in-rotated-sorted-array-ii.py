class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right)/2
                
            # greater than upper bound means mid is the rotated part so need to go to the right
            if nums[mid] > nums[right]:
                left = mid + 1
            
            # smaller than upper bound means mid is in the unrotated part and we need to go to the left
            elif nums[mid] < nums[right]:
                right = mid
             
            # if mid == upper limit, we dont know if min is in left or right so we decrease the upper bound by 1
            else:
                right -= 1
        
        return nums[left]