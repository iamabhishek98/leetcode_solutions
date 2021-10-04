import heapq

class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        m = {}
        for item in items:
            if item[0] not in m: m[item[0]] = [-item[1]]
            else: m[item[0]].append(-item[1])
        
        ans = []
        for key in m:
            count = 0
            avg = 0
            heapq.heapify(m[key])
            while count < 5 and m[key]:
                avg += (-1*heapq.heappop(m[key]))
                count += 1
            avg /= count
            ans.append([key,avg])
        
        ans.sort()
        return ans