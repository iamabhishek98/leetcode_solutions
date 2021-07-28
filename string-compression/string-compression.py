class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        left = 0
        count = 0
        while left < len(chars):
            right = left + 1
            while right < len(chars) and chars[left] == chars[right]:
                right += 1
            curr = right - left - 1
            if curr == 0: 
                count += 1
                left += 1
            else:
                temp = curr + 1
                while curr:
                    chars.pop(left+1)
                    curr -= 1
                    
                curr_arr = list(str(temp))
                for i in range(len(curr_arr)-1,-1,-1):
                    chars.insert(left + 1, curr_arr[i])
                
                count += temp
                left+=2
                
        
        return count
        