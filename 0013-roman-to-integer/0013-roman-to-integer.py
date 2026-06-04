class Solution(object):
    def romanToInt(self, s):
        

        result = 0
        n = len(s)
        di = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

        for i in range(0,n):
            if i < n-1 and di[s[i]] < di[s[i+1]]:
                result -= di[s[i]]
            else:
                result += di[s[i]]
        return result




          


        