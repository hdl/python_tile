from project3 import *
                            
	#YOUR CODE GOES HERE
def draw(width,height,letter,number):
	result=""
	temp=create(width,height,number)
	test=0
	for i in range(1,width*height+1):
		if(temp[test]==i):
			if(i%width==0):
				result=result+letter+"\n"
			else:
				result=result+letter
			test=test+1
		else:
			if(i%width==0):
				result=result+" "+"\n"
			else:
				result=result+" "			
	return result		
	
def soften(grid):
        count=0
        for i in range(3):
                for j in range(3):
                        if(grid[i][j]=="X"):
                                count=count+1
        return count



