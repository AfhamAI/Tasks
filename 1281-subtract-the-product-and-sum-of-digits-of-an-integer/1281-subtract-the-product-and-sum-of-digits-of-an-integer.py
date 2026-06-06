class Solution(object):
    def subtractProductAndSum(self, n):
        multi = 1
        sum = 0
        n = str(n)
        for i in n:
            multi *= int(i)
            sum += int(i)
            result = multi - sum
        return result
        