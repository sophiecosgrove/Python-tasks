invite = int(input('How many people do you want to invite? '))
if invite < 10:
    for i in range(invite):
        who = input('Enter the name: ')
        print(who + ' has been invited!')
else:
    print('Too many people!')