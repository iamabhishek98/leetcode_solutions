from collections import Counter

class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count_map = Counter(arr)
        count = 0
        curr_occurrences = 0
        for i in sorted(count_map.items(), key=lambda x: -x[1]):
            curr_occurrences += i[1]
            count += 1
            if curr_occurrences>=(len(arr)/2): return count
        return count
            
        