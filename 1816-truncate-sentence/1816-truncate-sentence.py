class Solution(object):
    def truncateSentence(self, s, k):
        s = s.split()
        li = []

        for i in range(0,k):
            li.insert(i,s[i])
        
        new = " ".join(li)
        return new


        