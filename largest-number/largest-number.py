class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                a = str(nums[i])+str(nums[j])
                b = str(nums[j])+str(nums[i])
                if (b > a):
                    nums[i],nums[j] = nums[j],nums[i]
        while len(nums)>1 and nums[0] == 0:
            nums.pop(0)
        return ''.join(map(str,nums))
