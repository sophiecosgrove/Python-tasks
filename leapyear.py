def isleapyear(year):
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        return year, 'is a leap year'
    else:
        return year, 'is not a leap year'

print(isleapyear(int(input('Enter a year: '))))


