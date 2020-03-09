
#This is a game that uses rock/paper/scissors logic and is to keep track of the user's and computers score. TODO!!! It will also ask you if you want to continue playing the game.
#Author Andrew Venenga
#Simple concept
#Corona beats flu
#flu beats ebola
#Ebola beats Corona


import random

computer_wins = 0
player_wins = 0

def Choose_Option():
    user_choice = input("Choose the Flu(F), CoronaVirus(C), or Ebola(E): ")
    if user_choice in ["Flu", "flu", "f", "F", "FLU"]:
        user_choice = "f"
    elif user_choice in ["CoronaVirus", "Coronavirus", "coronavirus", "c", "C", "CORONAVIRUS"]:
        user_choice = "c"
    elif user_choice in ["Ebola", "ebola", "e", "E", "EBOLA"]:
        user_choice = "e"
    else:
        print("Invalid entry, try again")
        Choose_Option()
    return user_choice

def Computer_Option():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "e"
    elif comp_choice == 2:
        comp_choice = "f"
    else:
        comp_choice = "c"
    return comp_choice

while True:
    print("")
    user_choice = Choose_Option()
    comp_choice = Computer_Option()
    print("")

    if user_choice =="c":

        if comp_choice =="c":
            print("I mean 2 Coronas are better then 1 ayyyyyyy. You tied.")

        elif comp_choice =="e":
            print("You chose the Coronavirus. The computer chose the Ebola. Chances are, you aren't going to make it. Computer wins.")
            computer_wins += 1
        
        elif comp_choice =="f":
            print("You chose the Coronavirus. The computer chose the Flu. ES CORONA TIME! You win.")
            player_wins += 1

    if user_choice =="f":

        if comp_choice =="f":
            print("Must be Flu season. You tied.")

        elif comp_choice =="c":
            print("You chose the Flu. The computer chose Coronavirus. Only one respiratory infection will kill this host, not you, Computer wins.")
            computer_wins += 1
        
        elif comp_choice =="e":
            print("You chose the Flu. The computer chose the Ebola. *cough cough* sorry forgot the shot this year. You win.")
            player_wins += 1

    if user_choice =="e":

        if comp_choice =="e":
            print("You both chose the Ebola. Uganda have a bad time.")

        elif comp_choice =="f":
            print("You chose the Ebola. The computer chose the Flu. The computer is right, you don't have ebola. Computer wins.")
            computer_wins += 1
        
        elif comp_choice =="c":
            print("You chose the Ebola. The computer chose the Corona. The Computer isn't up to date with the news. You win")
            player_wins += 1



user_choice = input("Do you want to play again? y/n")
if user_choice in ["Y", "y", "yes", "Yes"]:
    pass
elif user_choice in ["N", "n", "no", "No"]:
    "break"
else:
   "break"

