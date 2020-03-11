total_bugs = 0

for day in range(5):
    bugs = int(input("How many bugs did you collect today?\n"))
    total_bugs += bugs

print("\nYou have enslaved", format(total_bugs,",.0f"), "bugs.")