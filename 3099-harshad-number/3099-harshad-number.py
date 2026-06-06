class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        x = str(x)
        sum = 0
        for i in x:            
            sum += int(i)
    
        if int(x)%sum == 0:
            return sum
        else:
            return -1
            
