# This project contains user id and password validation
# Designed by Andrew Venenga

import sys
import re


def main():
    option()


def option():  # Basic menu
    print("------------Welcome to your username and password registration------------------")
    choice = input("""
    1: Login for returning users
    2: Registration for new user
    3: Reset current password.
    4: Exit.

    Enter your choice: """)
    if choice == '1':
        choice1()
    elif choice == '2':
        choice2()
    elif choice == '3':
        choice3()
    elif choice == '4':
        print("You have been logged out")
        input("Press enter to exit")
        sys.exit()
    else:
        print("Input invalid try again.\n\n")
        option()


def choice1():
    print("Login")
    username = input("Please enter your username\n")
    password = input("Please enter your password\n")
    for line in open("password.dat", "r").readlines():  # Read the lines
        login_info = line.split()  # Split on the space, and store the results in a list of two strings
        if username == login_info[0] and password == login_info[1]:
            print("Correct credentials!\n")
            input("Press enter to return to main menu\n")
            option()
    print("Incorrect credentials.\n")
    input("Press enter to return to main menu\n")
    option()


def choice2():
    unregex = re.compile("^[a-zA-Z]{6,10}[1-9]{2}$")  # compiling regex for username
    passregex = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")  # compiling regex for password
    condition = False
    condition2 = False
    while not condition:
        print("-Username must be between 6 and 10 characters, \n"
              "Must contain 2 numbers, \n"
              "NO WHITESPACE!\n  ")
        username = input("Please input your desired username \n")
        if unregex.search(username):
            print("Username is valid\n")
            condition = True
        else:
            print("Username invalid!!\n")
            condition = False

    while not condition2:  # Basic loop to test if the password matches the passregex
        print("-Password must be between 6-12 characters, \n"
              "Must contain 1 number \n"
              "Must have one uppercase letter and one lowercase\n"
              "Must NOT CONTAIN your username \n"
              "NO WHITESPACE!! \n")
        password = input("Please input your desired password \n")
        if password == username:  # if the password is the same as the username, the password is invalid
            print("Password must not be the same as your username!\n")
            condition2 = False
        elif passregex.search(password):  # if the password matches the regex, the password is valid.
            print("Password is valid \n")
            condition2 = True
        else:
            print("Password is invalid!!\n")
            condition2 = False
    try:  # try to open the file
        with open("password.dat", "a") as file:  # appends the file and adds the user
            file.write(username)
            file.write(" ")
            file.write(password)
            file.write("\n")
            file.close()
    except IOError:
        print('Missing password.dat file')
    print("Username and password has been created! \n")
    input("Press enter to return to the main menu \n")
    option()


def choice3():
    passregex = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")
    usernametodl = input("Please enter your username\n")
    passwordtodl = input("Please enter your password\n")
    condition = False
    while True:
        try:
            for lines in open("password.dat", "r").readlines():  # Read the lines
                login_info = lines.split()  # Split on the space, and store the results in a list of two strings
                if usernametodl == login_info[0] and passwordtodl == login_info[1]:  # username and password line
                    # split in a list
                    print("Correct credentials!\n")
                    while not condition:
                        print("-Password must be between 6-12 characters, \n"
                              "Must contain 1 number \n"
                              "Must have one uppercase letter and one lowercase\n"
                              "Must NOT CONTAIN your username \n"
                              "NO WHITESPACE!! \n")
                        password1 = input("Please input your desired password \n")
                        if password1 == usernametodl:
                            print("Password must not be the same as your username!\n")
                            condition = False
                        elif passregex.search(password1):
                            print("Password is valid\n")
                            condition = True
                            deleteLine(usernametodl, password1)
                        else:
                            print("Password is invalid!!\n")
                            condition = False
        except IOError:
            print('Missing password.dat file')
        print("Incorrect credentials.")
        input("Press enter to return to main menu\n")
        option()


def deleteLine(usernametodl, password1):
    output = []  # list for rewriting password.dat file
    fn = 'password.dat'
    try:
        f = open(fn)
        ##
        # this loop is designed to take everything currently in the password.dat file,
        # and overwrite the file with everything BUT the username and password being changed
        for line in f:
            if not line.startswith(usernametodl):
                output.append(line)
        f.close()
    except IOError:
        print('Missing password.dat file')
    try:
        f = open(fn, 'w')
        f.writelines(output)  # file rewritten
        f.close()
    except IOError:
        print('Missing password.dat file')
    try:
        with open("password.dat", "a") as f:  # new password is written to the end of the file
            f.write(usernametodl)
            f.write(" ")
            f.write(password1)
            f.write("\n")
            f.close()
    except IOError:
        print('Missing password.dat file')
    print("Password has been reset!")
    input("Press enter to return to the main menu.\n")
    option()


main()
