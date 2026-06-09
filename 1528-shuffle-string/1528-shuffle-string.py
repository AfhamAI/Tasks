class Solution(object):
    def restoreString(self, s, indices):
        li = [""]*len(s)
        for i in range(len(s)):
            li[indices[i]]=s[i]
        text = "".join(li)

        return text
