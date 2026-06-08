class Solution(object):
    def isPerfectSquare(self, num):
        
        i = 1
        n = 1
        while n <= num:
            n = i*i
            if num == n:
                return True
            i += 1
        return False
