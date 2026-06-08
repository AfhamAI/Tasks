class Solution(object):
    def reverseWords(self, s):
        s = s.split()
        li = []
        for i in s:
            i = i[::-1]
            li.append(i)
        result = " ".join(li)

        return result
