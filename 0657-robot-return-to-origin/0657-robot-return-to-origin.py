class Solution(object):
    def judgeCircle(self, moves):
        
        y = {
        "U" : 1,
        "D" : -1
        }
        x = {
        "R" : 1,
        "L" : -1
        }

        posY = 0
        posX = 0

        for i in moves:
            if i == "U" or i == "D":
                posY += y[i]
            else:
                posX += x[i]

        if posX == 0 and posY == 0:
            return True 
        else:
            return False

        

