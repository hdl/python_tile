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
        i=0
        while(i<len(grid)):
                j=0
                while(j<len(grid[i])):
                      if(grid[i][j]!="_"):
                              count=count+1         
                      j=j+1
                i=i+1
        if(grid[1][1]=='_'):
                count=count
        else:
                count=count-1
        return count



