class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in image:
            left = 0
            right = len(row)-1
            while left <= right:
                # flipping
                row[left], row[right] = row[right], row[left]
                
                # inverting
                row[left] = 0 if row[left] == 1 else 1
                if left != right: row[right] = 0 if row[right] == 1 else 1
                
                left += 1
                right -= 1

        return image