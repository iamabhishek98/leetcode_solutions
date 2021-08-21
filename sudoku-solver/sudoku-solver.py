from copy import deepcopy

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def checkPossibleValue(i,j,val):
            for r in range(9):
                if board[r][j] == val: return False
            
            for c in range(9):
                if board[i][c] == val: return False
            
            # find out which of the nine grids we are considering at that point in time
            gi = i // 3
            gj = j // 3
            for r in range(gi*3,gi*3+3):
                for c in range(gj*3, gj*3+3):
                    if board[r][c] == val: return False
            
            return True
        
        self.found = False
        self.solved = []
        
        def recurse():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for n in range(1,10):
                            if checkPossibleValue(i,j,str(n)):
                                board[i][j] = str(n)
                                recurse()
                                board[i][j] = "."
                        return
                    
            self.solved = deepcopy(board)          
    
        recurse()

        for i in range(9):
            for j in range(9):
                board[i][j] = self.solved[i][j]