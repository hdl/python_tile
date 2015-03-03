def checkTile(tile, number):

	#YOUR CODE HERE
    #always return false when tile is invalid
    if tile<1 or tile>12:
        return False

    if number == "one":
        if tile%3 == 0:
            return True
        else:
            return False
    if number == "two":
        if tile <=3 or tile==5 or tile==7 or tile>=10:
            return True
        else:
            return False
    if number == "three":
        if tile==4 or tile==7 or tile==8:
            return False
        else:
            return True
    if number == "four":
        if tile%3==0 or tile/3==1 or tile==1:
            return True
        else:
            return False
    if number == "five":
        if tile== 7 or tile == 8:
            return False
        else:
            return True

def isEmptyOnThree(tile, width):

	#YOUR CODE HERE
    if tile <1 or tile > 4*width or width<3:
        return "invalid"
    #top and bottom
    if tile <= width or tile>3*width:
        return False
    #second row
    elif tile >width and tile<=2*width:
        if tile > width+width/2 and tile<=2*width:
            return False
        else:
            return True
    #3rd row
    elif tile>2*width and tile<=3*width:
        if tile==3*width:
            return False
        else:
            return True
    else:
	    return True
