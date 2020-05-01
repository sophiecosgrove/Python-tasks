devsmoney = 100
devcanplaysmash = False

if devsmoney > 10 and devcanplaysmash:
    print('Dev enters a smash tornement!')
elif devsmoney < 1 and devcanplaysmash:
    print('Dev is too poor to enter')
else: 
    print('Dev just can\'t play smash')

mark = int(input('Enter your mark: '))

if mark >= 85:
    print('Distinction')
elif mark >= 65:
    print('Pass')
else:
    print('Fail')