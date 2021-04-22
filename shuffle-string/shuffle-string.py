class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        arr = ["" for i in range(len(s))]
        for i,x in enumerate(s):
            arr[indices[i]] = x
        return "".join(arr)