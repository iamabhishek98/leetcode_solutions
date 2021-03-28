class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 1: return intervals 
        intervals.sort()
        ans_list = []
        for i in intervals:
            status = False
            for j in ans_list:
                if i[0]<=j[0] and i[1]>=j[1]:
                    j[0] = i[0]
                    j[1] = i[1]
                    status = True
                elif i[0]<=j[0] and i[1] >= j[0] and i[1]<=j[1]:
                    j[0] = i[0]
                    status = True
                elif i[0]>=j[0] and i[0]<=j[1] and i[1]>=j[1]:
                    j[1] = i[1]
                    status = True
                elif i[0]>=j[0] and i[1]<=j[1]:
                    status = True
            if not status:
                ans_list.append(i)
        
        ans_set = set()
        for i in ans_list:
            ans_set.add((i[0],i[1]))
                    
        ans = []
        for i in ans_set:
            ans.append([i[0],i[1]])
        return ans