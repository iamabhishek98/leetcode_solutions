class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i,x in enumerate(nums):
            if nums[abs(x)-1] >=0:
                nums[abs(x)-1] = -nums[abs(x)-1]
            else:
                arr.append(abs(x))
        return arr