class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """        
        words = s.split(" ")
        sentence = ["" for _ in range(len(words))]
        
        for word in words:
            sentence[int(word[-1]) - 1] = word[:-1]
        
        return " ".join(sentence)
        