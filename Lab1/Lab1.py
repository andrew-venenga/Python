item1 = input("Enter price for item 1\n")
item2 = input("Enter price for item 2\n")
item3 = input("Enter price for item 3\n")
item4 = input("Enter price for item 4\n")
item5 = input("Enter price for item 5\n")

subtotal = item1 + item2 + item3 + item4 + item5
tax = 1.07 / subtotal
total = tax * subtotal

print("Your total is\n")
print()