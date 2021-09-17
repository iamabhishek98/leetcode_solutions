class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rl, rh, cl, ch = 0, len(matrix), 0, len(matrix[0])
        
        total = rh*ch
        count = 0
        traversal = []
        
        while count < total:
            for c in range(cl, ch):
                if matrix[rl][c] == 101: continue
                traversal.append(matrix[rl][c])
                matrix[rl][c] = 101
                count += 1
            
            rl += 1
            ch -= 1
            
            for r in range(rl, rh):
                if matrix[r][ch] == 101: continue
                traversal.append(matrix[r][ch])
                matrix[r][ch] = 101
                count += 1
            
            rh -= 1
            
            for c in range(ch, cl - 1, -1):
                if matrix[rh][c] == 101: continue
                traversal.append(matrix[rh][c])
                matrix[rh][c] = 101
                count += 1
            
            for r in range(rh, rl - 1, -1):
                if matrix[r][cl] == 101: continue
                traversal.append(matrix[r][cl])
                matrix[r][cl] = 101
                count += 1

            cl += 1            
        
        return traversal