keepGoing = True
while keepGoing:
    sales = float(input("enter the amount of sales: "))
    commRate = float(input("Enter the comission rate: "))
    commission = sales * commRate
    print ("The commison is $", format(commission, '10,.2f').sep='')
    ans = input("Do you want to calculate another comission (Enter y for yes): ")
    if ans.upper() == 'n'
        keepGoing = False
print("Thanks for playing")