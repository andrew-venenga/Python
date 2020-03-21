salary = 0.01
total = 0.01
time = 0.0

days = int(input("Enter the amount of days: "))

for days in range(days):
    print(days, "\t\t$", format(total, ".2f"), sep="")
    total = salary * 2
    salary = total
