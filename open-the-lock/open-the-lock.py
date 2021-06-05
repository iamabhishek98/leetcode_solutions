class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        # https://leetcode.com/problems/open-the-lock/discuss/1251924/Python-BFS-with-explantion-and-why-not-DFS
        
        deadends = set(deadends)
        q = ["0000"]
        visited = {}
        visited["0000"]=0
        
        while q:
            curr = q.pop(0)
            step = visited[curr]
            
            if curr in deadends: continue
            if curr == target: return step
            
            for i in range(4):
                nxt = curr[:i]+((str(int(curr[i])+1)) if int(curr[i])+1!=10 else '0')+curr[i+1:]
                if nxt not in visited:
                    visited[nxt] = step+1
                    q.append(nxt)
                    
                nxt = curr[:i]+((str(int(curr[i])-1)) if int(curr[i])-1!=-1 else '9')+curr[i+1:]
                if nxt not in visited:
                    visited[nxt] = step+1
                    q.append(nxt)
                
        return -1 