class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # if dealing with unique values, always use sets
        seen = set()
        
        for i in range(9):
            col_set = set()
            for j in range(9):
                if board[i][j] != ".":
                    row = board[i][j] + "found in row" + str(i)
                    col = board[i][j] + "found in col" + str(j)
                    quadrant = board[i][j] + "found in quadrant" + str(i/3) + " " + str(j/3)
                    
                    if row in seen or col in seen or quadrant in seen: return False
                    
                    seen.add(row)
                    seen.add(col)
                    seen.add(quadrant)
        
        return True