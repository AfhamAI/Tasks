class Solution(object):
    def smallestEvenMultiple(self, n):

        ans = None
        li = []
        for i in range(1,11):
            ans = n*i
            li.append(ans)
        for i in li:
            if i%2==0:
                return i
                break
