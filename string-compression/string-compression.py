class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # https://www.youtube.com/watch?v=IhJgguNiYYk&ab_channel=KevinNaughtonJr.
        
        # approach is to keep overwriting the previous characters
        # the returned new length of the string is the part of the string tht will be considered for the solution
        
        index = 0
        left = 0
        
        while left < len(chars):
            right = left + 1
            while right < len(chars) and chars[left] == chars[right]:
                right += 1
            
            # index is incremented because the current char has already been written
            chars[index] = chars[left]
            index += 1
            
            curr = right - left
            if curr > 1: 
                for i in str(curr):
                    chars[index] = i
                    index += 1
                    
            left = right
                
        
        return index
        