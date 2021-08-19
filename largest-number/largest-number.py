class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        nums = sorted(map(str,nums),cmp=(lambda x,y : 1 if x+y < y+x else -1))
        res = ''.join(nums)
        # the most significant number will be in front so if 0 is in front, we return 0 as we know the result is a string of 0s
        return '0' if res[0] == '0' else res
    