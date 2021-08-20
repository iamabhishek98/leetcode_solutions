class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # if dealing with unique values, always use sets
        seen = set()
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    # these values will always remain distinct
                    row = board[i][j] + "row" + str(i)
                    col = board[i][j] + "col" + str(j)
                    quadrant = board[i][j] + "quad" + str(i/3) + str(j/3)
                    
                    if row in seen or col in seen or quadrant in seen: return False
                    
                    seen.add(row)
                    seen.add(col)
                    seen.add(quadrant)
        
        return True