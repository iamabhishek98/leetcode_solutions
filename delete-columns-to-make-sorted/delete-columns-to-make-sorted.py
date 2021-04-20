class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        i = 0
        count = 0
        while i < len(strs[0]):
            prev = strs[0][i]
            for j in strs:
                if j[i] < prev:
                    count += 1
                    break
                prev = j[i]
            i+=1
        return count
        