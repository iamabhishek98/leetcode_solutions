class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0 # pointer for even misplaced
        j = 1 # pointer for odd misplaced
        
        # invariant: for every misplaced odd there is misplaced even
        # since there is just enough space for odds and evens
        
        while i < len(nums) and j < len(nums):
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                # nums[i] % 2 == 1 and nums[j] % 2 == 0
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2
                
        return nums