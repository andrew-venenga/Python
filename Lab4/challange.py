for row in range(7, 0, -1):
    for column in range(row, 0, -1):
        print ("*", end="")
    print()

for row in range(6):
    print ("#", end="", sep="")
    for spaces in range( row ):
        print(" ", end="", sep="")
    print("#", sep="")