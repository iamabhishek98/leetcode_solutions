from sortedcontainers import SortedDict

class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        m = SortedDict()
        for i in range(len(mat)):
            c = mat[i].count(1)
            if c not in m: 
                m[c] = [i]
            else: m[c].append(i)
        
        arr = []
        status = True
        for i in m:
            if not status: break
            for j in m[i]:
                if len(arr) == k: 
                    status = False
                    break
                arr.append(j)
                
        return arr