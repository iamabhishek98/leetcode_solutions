class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        moves = [[1,0],[-1,0],[0,1],[0,-1]]
        
        def backtrack(i,j,idx=0):
            if idx == len(word): return True
            
            if not (0<=i<m and 0<=j<n) or board[i][j]!=word[idx]: return False
            
            # mark it as visited
            board[i][j] = "#"
            
            for move in moves:
                # check if backtracking in any of the directions is successful
                res = backtrack(i+move[0],j+move[1],idx+1)
                
                # no need to check other directions if any one direction has successful backtracking
                if res: break
              
            # backtrack and undo the marking
            board[i][j] = word[idx]
            
            return res
        
        for i in range(m):
            for j in range(n):
                if backtrack(i,j): return True
            
        return False