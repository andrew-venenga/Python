##Andrew Venenga 03/02/2020 Lab 2
#This program takes the input from the user, input being the amount of packages the user purchase
#and then calculates and displays the amount of a discount the user would recieve.

number = int(input('Enter the number of packages you purchased '))
#Takes input of the user

#Discount is calculated based off what the user entered
if number >= 100:
    print('Discount amount is 40% plus the total amount of the purchase... '
          'The total after the discount is $', 99 * number * 0.6, sep='')
#Elif is used if the previous condition isnt true, these conditions will be tested.
elif number >= 50 and number <= 99:
    print('Discount amount is 30% plus the total amount of the purchase... '
          'The total after the discount is $', 99 * number * 0.7, sep='')
elif number >= 20 and number <= 49:
    print('Discount amount is 20% plus the total amount of the purchase... '
          'The total after the discount is $', 99 * number * 0.8, sep='')
elif number >= 10 and number <= 19:
    print('Discount amount is 10% plus the total amount of the purchase... '
          'The total after the discount is $', 99 * number * 0.9, sep='')
else:
    print('Discount amount is 0% plus the total amount of the purchase... '
          'The total after the discount is $', 99 * number, sep='')