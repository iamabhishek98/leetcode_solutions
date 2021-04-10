class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        pi = si = pj = 0
        sj = len(mat)-1
        s = 0
        while pi < len(mat) and pj < len(mat):
            s += mat[pi][pj]
            if pi != si or pj != sj:
                s += mat[si][sj]
            pi += 1
            pj += 1
            si += 1
            sj -= 1
        return s
            