class Solution(object):
    def findGCD(self, nums):
        largest = max(nums)
        smallest = min(nums)
        divisors = []
        for i in range(1,smallest+1):
            if smallest%i==0 and largest%i==0:
                divisors.append(i)

        return max(divisors)
