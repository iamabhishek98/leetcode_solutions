def addZeros(s,n):
    while(n):
        s+="0"
        n-=1
    return s

def addSum(num1,num2):
    r1 = num1[::-1]
    r2 = num2[::-1]
    if (len(r1)<len(r2)):
        r1 = addZeros(r1,len(r2)-len(r1))
    elif (len(r2)<len(r1)):
        r2 = addZeros(r2,len(r1)-len(r2))
    c = 0
    sum = ""
    i = 0
    while (i < len(r1)):
        t = int(r1[i])+int(r2[i])+c
        if (t>=10):
            c = 1
            sum+=str(t%10)
        else:
            c = 0
            sum+=str(t)
        i+=1
    if (c == 1):
        sum+="1"
    return sum[::-1]

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        products = []
        
        for i in range(len(num1)-1,-1,-1):
            num_zeros = len(num1)-1-i
            carry = 0
            curr_product = ""
            for _ in range(num_zeros):
                curr_product += "0"
            for j in range(len(num2)-1,-1,-1):
                product = int(num1[i])*int(num2[j])+carry
                carry = 0
                if j != 0:
                    curr_product += str(product % 10)
                    carry = product / 10
                else:
                    if product < 10:
                        curr_product += str(product)
                    else:
                        curr_product += str(product%10) + str(product/10)
            products.append(curr_product[::-1])

        i = 0
        while i < len(products)-1:
            a = products[i]
            b = products[i+1]
            s = addSum(a,b)
            products[i+1] = s
            i += 1
        
        return '0' if products[-1][0] == '0' else products[-1]