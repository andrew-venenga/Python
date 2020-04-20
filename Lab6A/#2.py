#Open the file in read mode
import sys
try:
    file_obj = open('golf.dat', 'r')
except IOError as e:
    print(e)
    print(sys.exc_type)

#Read name of first record and remove trailing new line escape sequence

name = file_obj.readline().rstrip('\n')


#Print header far table

print('\n' + '\033[4m' + 'Name               Score' + '\033[0m')

#keep retrieving and printing names and scores from the file until the EOF while name !=":

score = int(file_obj.readline())

print(format(name, '12s'), format(score, '>10d')) #align

name = file_obj.readline().rstrip('\n')

# Close the file

file_obj.close()
