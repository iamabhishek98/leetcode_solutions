from collections import deque

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversed_words = deque()
        curr_word = ""
        
        for i,x in enumerate(s):
            if x == " ":
                if len(curr_word):
                    reversed_words.appendleft(curr_word)
                    curr_word = ""
            elif x != " " and i == len(s)-1:
                curr_word += x
                reversed_words.appendleft(curr_word)
            else:
                curr_word += x

        return ' '.join(reversed_words)