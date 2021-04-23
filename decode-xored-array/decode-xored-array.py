class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        arr = [first]
        for i in range(len(encoded)):
            x = arr[i]^encoded[i]
            arr.append(x)
        return arr