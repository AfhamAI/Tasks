class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        diagonals = 0
        large = 0
        largeLen = 0
        largeWid = 0
        largeArea = 0
        
        for i in dimensions:
            length = i[0]
            width = i[1] 
            area = length*width
            diagonal = (sqrt((length*length) + (width*width))) 
            if large < diagonal:
                large = diagonal
                largeLen = length
                largeWid = width
                largeArea = area
            elif large == diagonal:
                if largeArea < area:
                    large = diagonal
                    largeLen = length
                    largeWid = width
                    largeArea = area
                    
                
        return largeLen * largeWid
                






        # length1 = dimensions[0][0] 
        # width1 = dimensions[0][1] 
        # diagonal1 = sqrt((length1*length1) + (width1*width1)) 

        # length2 = dimensions[1][0] 
        # width2 = dimensions[1][1] 
        # diagonal2 = sqrt((length2*length2) + (width2*width2)) 

        # if diagonal1 == diagonal2:
        #     return length1*width1
        # elif diagonal1 > diagonal2:
        #     return length1*width1
        # else:
        #     return length2*width2
        

            