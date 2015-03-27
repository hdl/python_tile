def create (width,height,number):
    result=[]
    if number == "one":
        count = 1
        while(count <= width * height):
            if count%width==0:
                result.append(count)
            count = count +1
    if number == "two":
        #first line
        count = 1
        while(count <= width):
            result.append(count)
            count = count +1
        #last line
        count=width*(height-1)+1
        while(count <= width*height):
            result.append(count)
            count = count +1

        #middle line
        middle = (height+1)/2
        count = width*(middle-1)+2
        while(count < middle*width):
            result.append(count)
            count = count + 1;

        #right column
        count=2
        while(count < middle):
            result.append(count*width)
            count = count+1
        #left colum
        count = middle+1
        while(count < height):
            result.append((count-1)*(width)+1)
            count = count +1
    if number=="three":
        #first line
        count=1
        while(count<=width):
            result.append(count)
            count=count+1
        #last line
        count=(height-1)*width+1
        while(count<=width*height):
            result.append(count)
            count=count+1

        #right column
        count=2*width
        while(count<height*width):
            result.append(count)
            count=count+width

        #middle line
        #middleH is middleHeight
        #middleW is middleWidth
        middleH=(height+1)/2
        middleW=(width+1)/2
        if(width%2==0):
            count=(height+1)/2*width-width/2+1
            while(count<width*middleH):
                result.append(count)
                count=count+1
        else:
            count=(height+1)/2*width-width/2
            while(count<width*middleH):
                result.append(count)
                count=count+1
    
    if number=="four":
        #right column
        count=1
        while(count<=height):   
            result.append(count*width)
            count=count+1
            
        #middle line    
        middle=(height+1)/2
        count=(middle-1)*width+1
        while(count<(middle*width)):
            result.append(count)
            count=count+1

        #left column  
        count=1
        middle=(height+1)/2
        while(count<(middle-1)*width+1):
            result.append(count)
            count=count*width+1

    if number=="five":
            #first line
            count=1
            while(count<=width):
                result.append(count)
                count=count+1
            #last line
            count=(height-1)*width+1
            while(count<=width*height):
                result.append(count)
                count=count+1
            #middle line
            middle=(height+1)/2
            count=width*(middle-1)+2
            while(count<middle*width):
                result.append(count)
                count=count+1
            #left colunm
            count=width+1
            while(count<=(middle-1)*width+1):
                result.append(count)
                count=count+width
            #right column
            count=width*middle
            while(count<width*height):
                result.append(count)
                count=count+width

    result.sort()
    return result
            
