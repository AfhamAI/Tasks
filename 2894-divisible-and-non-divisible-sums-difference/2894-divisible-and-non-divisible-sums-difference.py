class Solution(object):
    def differenceOfSums(self, n, m):
        divisible = 0
        nonDivisible = 0
        for i in range(1,n+1):
            if i%m==0:
                divisible += i
            else:
                nonDivisible += i

        result = nonDivisible - divisible
        return result
