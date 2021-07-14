class Solution(object):
    def customSortString(self, order, str):
        """
        :type order: str
        :type str: str
        :rtype: str
        """
        order_map = {}
        for i,x in enumerate(order):
            order_map[x] = i
        
        arr = list(str)
        
        def compare(a):
            if a in order_map: return order_map[a]
            return 0
        
        return ''.join(sorted(arr,key=compare))
        
        