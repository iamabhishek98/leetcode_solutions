class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # (a+ib)(x+iy) = ax+i^2by+i(bx+ay) = ax−by+i(bx+ay)
        n1 = num1.split("+")        
        n2 = num2.split("+")

        a = int(n1[0])
        # remove i from end of string
        b = int(n1[1][:-1])
        
        x = int(n2[0])
        y = int(n2[1][:-1])
        
        return str(a*x - b*y)+"+"+str(b*x+a*y)+"i"
        