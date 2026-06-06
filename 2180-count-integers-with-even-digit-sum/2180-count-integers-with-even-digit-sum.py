class Solution(object):
    def countEven(self, num):
        count= 0
        
        for i in range (1,num+1):
            sum = 0
            st = str(i)
            for j in st:
                j = int(j)
                sum += j
            if sum % 2 == 0:
                count += 1
        return count