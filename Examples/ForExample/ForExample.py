for num in (1, 2, 3, 4):
    print(num)

for name in ('Winken', 'Blinken', 'Nod'):
    print(name)

for num in range(5):
    print(num)

for num in range(1, 5):
    print(num)

print("\n")
for num in range(1,6,2):
    print(num)

print("\n")
for num in range(5,0,-1):
    print(num)

num = num + 1
print(num)

num %= 5
print(num)

print("^^^^^^^^^^^^^^^^^")

print("this program displays a list of numbers")
print("starting at 1) and their squares")
end = int(input('How high should I go?'))

print()
print('Number\tSquare')
print('-----------------------')

total = 0
for number in range(1, end + 1):
    square = number**2
    print(number, '\t', format(square, '5,d'))
    total += square