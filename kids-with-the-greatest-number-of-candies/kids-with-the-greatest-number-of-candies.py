class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        m = max(candies)
        ans = []
        for i in candies:
            status = False
            if i+extraCandies>=m: status = True
            ans.append(status)
        return ans
        