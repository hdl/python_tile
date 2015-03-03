def create (width, height, number):
    result = []

    #YOUR CODE GOES HERE
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

    result.sort()
    return result
