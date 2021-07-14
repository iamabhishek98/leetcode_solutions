from collections import Counter

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
        
        # bucket sort
        freq = {}
        for i in range(len(order)):
            freq[i] = []
        
        ans = []
        for i in str:
            if i in order_map: freq[order_map[i]].append(i)
            else: ans.append(i)
        
        for i in freq:
            ans.extend(freq[i])
        
        return ''.join(ans)
        
        
        