import sys
try:
    file_obj = open('golf.dat', 'w')
except IOError as e:
    print(e)
    print(sys.exc_type)


def main():
    enterAgain = "y"
    while enterAgain == 'y' or enterAgain == 'Y':
        name, score = inp()
        output(name, score)

        print('Do you wish to enter another player?')
        enterAgain = input("'Y' = yes, anything else = 'no': ")
    # Close file
    file_obj.close()
    print('Program ended')

def inp():
# Get the first player's name
    name = input('Enter the name of a golfer or enter q if you\'re done: ')

    while name != 'q' and name != 'Q':
        # Get the player's score

        try:
            score = int(input('Enter the golf score of player ' + name +': '))
            break
        except ValueError:
            print('Number entered is invalid, Please try again: ')
    return name, score




def output(name, score):
# Write a record of the player's name and score
        file_obj.write(name + '\n')
        file_obj.write(str(score)+ '\n')

main()

