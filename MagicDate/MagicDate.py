#this program tells if the month times the date = the year. If this happens to be true this date is 'magic'
month = int(input('Enter a month in numeric form: '))
day = int(input('Enter a day in numeric form: '))
year = int(input('Enter a two-digit year in numeric form: '))

if month * day == year:
    print('The date is magic.')
else:
    print('The date is not magic.')