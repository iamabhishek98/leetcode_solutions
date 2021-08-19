class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # we sort this way instead of descending order because the number can have more than 1 digit in which case, there might be edge cases
        # e.g. take 30 and 3. descending order gives 303 but we want 330 so we use pairwise comparison for each sort: 303 < 330
        nums = sorted(map(str,nums),cmp=(lambda x,y : 1 if x+y < y+x else -1))
        res = ''.join(nums)
        # the most significant number will be in front so if 0 is in front, we return 0 as we know the result is a string of 0s
        return '0' if res[0] == '0' else res
    