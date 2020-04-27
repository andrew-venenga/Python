# This project contains user id and password validation
# Designed by Andrew Venenga
import csv
import os
import sys
import re
import tempfile

try:
    file_obj = open('password.dat', 'a')

except IOError as e:
    print(e)
    print(sys.exc_type)


def main():
    option()


def option():
    print("Welcome to your username and password registration")
    choice = input("""
    1: to login with your current username and password
    2: for new User
    3: to reset your password.
    4: to exit.

    Enter your choice: """)
    if choice == '1':
        choice1()
    elif choice == '2':
        choice2()
    elif choice == '3':
        choice3()
    elif choice == '4':
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
            print("Correct credentials!")
            input("Press enter to return to main menu\n")
            option()
        elif print("Incorrect credentials."):
            input("Press enter to return to main menu\n")
            option()


def choice2():
    unregex = re.compile("^[a-zA-Z]{1,10}[1-9]{2}$")  # compiling regex for username
    passregex = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")  # compiling regex for password
    condition = False
    condition2 = False
    while not condition:
        username = input("Please input your desired username \n")
        if unregex.search(username):
            print("Username is valid")
            condition = True
        else:
            print("Username invalid!!")
            condition = False

    while not condition2:
        password = input("Please input your desired password \n")
        if password == username:
            print("Password must not be the same as your username!")
            condition2 = False
        elif passregex.search(password):
            print("Password is valid")
            condition2 = True
        else:
            print("Password is invalid!!")
            condition2 = False
    try:
        with open("password.dat", "a") as file:
            file.write(username)
            file.write(" ")
            file.write(password)
            file.write("\n")
            file.close()
    except IOError:
        print('Missing password.dat file')
    input("Press enter to return to the main menu \n")
    option()
    if choice1():
        print("You are now logged in...\n")
        input("Press enter to return to main menu\n")
        main()
    else:
        print("You aren't logged in!\n")
        main()

###
# TODO figure out how to move everything from password.dat to a list,
#  then convert that list into a temp file to rewrite password.dat
def choice3():
    print("Testing choice 3")
    updated_list = []
    cached_list = []

    with open("password.dat", "r") as f:
        lines = f.read().splitlines()

        reader = list(csv.reader(f))  # Convert iterable to list to make things easier.
        print("CHANGE PASSWORD?!")
        username = input("Enter the username for the required user: ")
        cached_list = reader  # store copy of data.

        for row in reader:  # for every row in the file
            for field in row:
                if field == username:  # if a field is == to the required username
                    updated_list.append(row)  # add each row, line by line, into a list called 'updated_list'
                    newpassword = input("Enter new password: ")
                    # print(updatedlist[0][1]) (this is how we get at the password field, noting it is a nested list)
                    updated_list[0][1] = newpassword  # set the field for password to the new password

        update_password(updated_list, cached_list)


def update_password(updated_list, cached_list):
    for index, row in enumerate(cached_list):
        for field in row:
            if field == updated_list[0][0]:
                cached_list[index] = updated_list  # Replace old record with updated record.

    with open("password.dat", "w") as f:
        writer = csv.writer(f)
        writer.writerows(cached_list)
        print("File has been updated")


main()
