class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i,x in enumerate(nums):
            if x not in map: map[x] = [i]
            else: map[x].append(i)
        
        for x in nums:
            if target-x == x:
                if len(map[x]) >= 2:
                    return [map[x][0],map[x][1]]
            elif target-x in map:
                return [map[x][0],map[target-x][0]]