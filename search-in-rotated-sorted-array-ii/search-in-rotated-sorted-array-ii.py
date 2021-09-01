class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums) - 1
        
        if target == nums[0] or target == nums[-1]: return True
        
        while left < right:
            # to remove duplicates
            while left < right and nums[left] == nums[left+1]: left += 1
            while left < right and nums[right] == nums[right-1]: right -= 1
                
            mid = (left + right)/2
            
            if nums[mid] == target: return mid
            
            # target might be in rotated part
            if target > nums[0]:
                # we are in rotated part
                if nums[mid] > nums[0]:
                    if target < nums[mid]:
                        right = mid
                    else:
                        left = mid + 1
                
                # we are in unrotated part so we need to go left regardless
                else:
                    right = mid
                    
            # target might be in unrotated part
            else:
                # we are in rotated part so we need to go right regardless
                if nums[mid] > nums[0]:
                    left = mid + 1
                
                # we are in unrotated part
                else:
                    if target < nums[mid]:
                        right = mid
                    else:
                        left = mid + 1
            
        return nums[left] == target