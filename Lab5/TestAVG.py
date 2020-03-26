testOne = int(input('Enter a score for test one: '))
testTwo = int(input('Enter a score for test two: '))
testThree = int(input('Enter a score for test three: '))
testFour = int(input('Enter a score for test four: '))
testFive = int(input('Enter a score for test five: '))

def calcAverage(testOne, testTwo, testThree, testFour, testFive):
    average = (testOne + testTwo + testThree + testFour + testFive) / 5
    return average

def determineGrade(testOne, testTwo, testThree, testFour, testFive):
    for i in testOne, testTwo, testThree, testFour, testFive:
        if 90 <= i:
            print('The grade of', i, 'is A')
        elif 80 <= i and i <= 89:
            print('The grade of', i, 'is B')
        elif 70 <= i and i <= 79:
            print('The grade of', i, 'is C')
        elif 60 <= i and i <= 69:
            print('The grade of', i, 'is D')
        elif i < 60:
            print('The grade of', i, 'is F')
average = calcAverage(testOne, testTwo, testThree, testFour, testFive)
print('The average of your scores is', average)
determineGrade(testOne, testTwo, testThree, testFour, testFive)