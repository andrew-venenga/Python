# This project contains user id and password validation
# Designed by Andrew Venenga
import sys
try:
    file_obj = open('password.dat', 'w')
except IOError as e:
    print(e)
    print(sys.exc_type)

def main():
    option()


def option():
    print("Welcome to your username and password registration")
    choice = input("Enter 1 to login with your current username and password \n"
     "Enter 2 for new User \n"
     "Enter 3 to reset your password. \n")
    if(choice == '1'):
        choice1()
    elif(choice == '2'):
        choice2()
    elif(choice == '3'):
        choice3()
    else:
        print("Input invaid try agian.\n\n")
        option()

def choice1():
    print("Login")
    username = input("Please enter your username\n")
    password = input("Please enter your password\n")
    for line in open("password.dat","r").readlines(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        if username == login_info[0] and password == login_info[1]:
            print("Correct credentials!")
            input("Press enter to return to main menu\n")
            return True
        elif print("Incorrect credentials."):
            input("Press enter to return to main menu\n")
            return False


def choice2():
    username = input("Please input your desired username \n")
    password = input("Please input your desired password \n")
    file = open("password.dat","a")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    if choice1():
        print("You are now logged in...\n")
        input("Press enter to return to main menu\n")
        main()
    else:
        print("You aren't logged in!\n")
        main()

def choice3():
    print("Testing choice 3")


main()