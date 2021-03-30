class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_arr = sorted(arr)
        ans = []
        m = {}
        rank = 1
        for i,x in enumerate(sorted_arr):
            if not len(m): m[x] = 1
            else:
                if x==sorted_arr[i-1]:
                    continue
                rank+=1
                m[x] = rank
        
        for i in arr:
            ans.append(m[i])
        return ans
        